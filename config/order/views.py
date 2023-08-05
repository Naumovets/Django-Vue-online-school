import calendar
import json

from django.db.models import Count
from django.http import Http404
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import permission_classes, authentication_classes
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from cart.models import Coupon, UsedCoupon, Cart
from cart.serializers import CartItemForPriceSerializer
from cart.services.cart_manager import CartManager
from config.settings import TERMINAL_KEY
from course.models import Course, Curator
from order.models import Order, OrderItem, ConfirmedCourse
from datetime import date, timedelta

from order.serializers import TinkoffResponseSerializer
from order.services.order_manager import OrderManager


@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
class addFreeCourseOrderItem(APIView):

    def post(self, request, course_id):
        """ Добавление бесплатных курсов в модель оплаченных (confirmed) """
        user = request.user
        course = get_object_or_404(Course,
                                   id=course_id,
                                   status=Course.Status.FREE)
        if ConfirmedCourse.objects.filter(user=user, course=course).exists():
            return Http404()
        ConfirmedCourse.objects.create(user=user,
                                       course=course,
                                       create_date=date.today(),
                                       update_date=date.today(),
                                       end_date=date.today() + timedelta(365))
        return Response()


@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
class addOrderItems(APIView):

    def post(self, request, coupon_code=None):
        """ Создание заказа с курсами """
        user = request.user
        if Coupon.objects.filter(code=coupon_code).exists():
            coupon = Coupon.objects.get(code=coupon_code)
            if UsedCoupon.objects.filter(user=user, coupon=coupon).exists():
                coupon = None
        else:
            coupon = None

        json_parsed_courses = json.loads(request.body)
        if len(json_parsed_courses) < 1:
            return Http404()

        # { 'array': [{'period': period, 'id': id},...], 'promocode': promocode }

        data_of_courses = CartItemForPriceSerializer(data=json_parsed_courses, many=True)
        data_of_courses.is_valid()
        total_price = CartManager.get_total_price(user=user,
                                                  coupon_code=coupon_code,
                                                  data_of_courses=data_of_courses.validated_data)
        result_price = total_price['result_price']
        if Cart.objects.get(user=user).items.all().exists():
            order = Order.objects.create(user=user,
                                         coupon=coupon,
                                         result_price=result_price)

            courses_titles = []
            many = data_of_courses.validated_data > 1
            for data in data_of_courses.validated_data:
                course = Course.objects.get(id=data['id'])

                period = OrderItem.Period.FULL if data['period'] == 'full' else OrderItem.Period.MONTH,
                result_price = OrderManager.get_result_price(course=course, coupon=coupon, period=period, many=many)

                OrderItem.objects.create(order=order,
                                         course=course,
                                         period=period,
                                         result_price=result_price)
                courses_titles.append(course.title + ' ' + course.get_status_display() + ' ' + str(course.subject.exam))

            description = 'Набор курсов: ' + ', '.join(courses_titles)
            CartManager.clear_cart(user=user)
            return Response({'id': order.id,
                             'price': result_price,
                             'description': description})
        else:
            return Http404()


class UpdateOrderStatus(APIView):

    def post(self, request):
        json_tinkoff_response = json.loads(request.body)
        tinkoff_response = TinkoffResponseSerializer(data=json_tinkoff_response)
        tinkoff_response.is_valid()

        terminal_key = tinkoff_response.validated_data['TerminalKey']
        order_id = tinkoff_response.validated_data['OrderId']
        success = tinkoff_response.validated_data['Success']
        status = tinkoff_response.validated_data['Status']

        # Идентификатор платежа в системе банка
        payment_id = tinkoff_response.validated_data['PaymentId']

        # Код ошибки (если ошибки не произошло, передается значение «0»)
        error_code = tinkoff_response.validated_data['ErrorCode']
        amount = tinkoff_response.validated_data['Amount']

        # Идентификатор автоплатежа
        rebill_id = tinkoff_response.validated_data['RebillId']

        # Идентификатор сохраненной карты в системе банка
        card_id = tinkoff_response.validated_data['CardId']

        # Замаскированный номер карты/Замаскированный номер телефона
        pan = tinkoff_response.validated_data['Pan']

        # Срок действия карты (в формате MMYY, где YY — две последние цифры года)
        exp_date = tinkoff_response.validated_data['ExpDate']

        # См. Подпись запроса (https://www.tinkoff.ru/kassa/develop/api/request-sign/)
        token = tinkoff_response.validated_data['Token']

        order = get_object_or_404(Order, id=order_id)
        order.terninal_key = terminal_key
        order.paid = success
        order.status = status
        order.payment_id = payment_id
        order.error_code = error_code
        order.amount = amount
        order.rebill_id = rebill_id
        order.card_id = card_id
        order.pan = pan
        order.exp_date = exp_date
        order.token = token
        order.save(update_fields=['paid', 'status', 'payment_id', 'error_code', 'amount', 'rebill_id', 'card_id', 'pan',
                                  'exp_date', 'token'])

        if order.paid:

            user = order.user

            # Добавление купона в список использованных
            if order.coupon:
                if not UsedCoupon.objects.filter(user=user, coupon=order.coupon).exists():
                    UsedCoupon.objects.create(user=user,
                                              coupon=order.coupon)

            # Получение всех курсов в заказе
            order_items = order.items.all()
            many = len(order_items) > 1

            for order_item in order_items:
                result_price = OrderManager.get_result_price(course=order_item.course,
                                                             coupon=order.coupon,
                                                             period=order_item.period,
                                                             many=many)

                # Дата окончания действия курса = сегодня + месяц или год в зависимости от периода действия в заказе
                if ConfirmedCourse.objects.filter(user=user, course=order_item.course).exists():

                    confirmed_course = ConfirmedCourse.objects.get(user=user, course=order_item.course)

                    if order_item.period == OrderItem.Period.FULL:
                        end_date = date(date.today().year + 1, date.today().month, date.today().day)
                    else:
                        if confirmed_course.end_date >= date.today():
                            end_date = confirmed_course.end_date + timedelta(30)
                        else:
                            end_date = date.today() + timedelta(days=30)

                    confirmed_course.coupon = order.coupon if order.coupon else None
                    confirmed_course.result_price = result_price
                    confirmed_course.update_date = date.today()
                    confirmed_course.end_date = end_date
                    confirmed_course.save()
                else:
                    if order_item.period == OrderItem.Period.FULL:
                        end_date = date(date.today().year + 1, date.today().month, date.today().day)
                    else:
                        if date.today().month in [7, 8]:
                            end_date = date(date.today().year, 10, 1)
                        else:
                            end_date = date.today() + timedelta(days=30)

                    curator = Curator.objects \
                        .filter(course=order_item.course) \
                        .annotate(count_students=Count('curator_orders')) \
                        .order_by('curator_orders') \
                        .first()
                    ConfirmedCourse.objects.create(user=user,
                                                   course=order_item.course,
                                                   coupon=order.coupon,
                                                   result_price=result_price,
                                                   create_date=date.today(),
                                                   update_date=date.today(),
                                                   end_date=end_date,
                                                   curator=curator)

        return Response('OK')
