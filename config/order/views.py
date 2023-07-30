import calendar
import json

from django.db.models import Count
from django.http import Http404
from phonenumbers import format_number, PhoneNumberFormat
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import permission_classes, authentication_classes
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from cart.models import Coupon, UsedCoupon, Cart
from cart.serializers import CartItemForPriceSerializer
from cart.services.cart_manager import CartManager
from course.models import Course, Curator
from order.models import Order, OrderItem, ConfirmedCourse
from datetime import date, timedelta

from order.services.order_manager import OrderManager


@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
class addFreeCourseOrderItem(APIView):

    def post(self, request, course_id):
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
            for data in data_of_courses.validated_data:
                course = Course.objects.get(id=data['id'])
                OrderItem.objects.create(order=order,
                                         course=course,
                                         period=OrderItem.Period.FULL if data['period'] == 'full' else OrderItem.Period.MONTH)
                courses_titles.append(course.title)

            description = ', '.join(courses_titles)

            # CartManager.clear_cart(user=user)
            return Response({'id': order.id,
                             'price': result_price,
                             'phone': format_number(user.tel, PhoneNumberFormat.E164),
                             'description': description})
        else:
            return Http404()


class ConfirmOrder(APIView):
    def post(self, request, order_id):
        """ Метод обновляет статус оплаты заказа и добавляет/обновляет оплаченные курсы пользователю """

        order = get_object_or_404(Order, id=order_id)
        order.paid = True
        order.save()

        user = order.user
        if order.coupon:
            if not UsedCoupon.objects.filter(user=user, coupon=order.coupon).exists():
                UsedCoupon.objects.create(user=user,
                                          coupon=order.coupon)
        order_items = order.items.all()
        many = len(order_items) > 1
        for order_item in order_items:
            price_with_discount = OrderManager.get_price_with_discount(course=order_item.course,
                                                                       coupon=order.coupon,
                                                                       many=many)
            # Дата окончания действия курса = сегодня + месяц или год в зависимости от периода действия в заказе

            if ConfirmedCourse.objects.filter(user=user, course=order_item.course).exists():

                confirmed_course = ConfirmedCourse.objects.get(user=user, course=order_item.course)

                if order_item.period == OrderItem.Period.FULL:
                    end_date = date(date.today().year + 1, date.today().month, date.today().day)
                else:
                    end_date = confirmed_course.end_date + timedelta(30)

                confirmed_course.coupon = order.coupon if order.coupon else None
                confirmed_course.price_with_discount = price_with_discount
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

                curator = Curator.objects\
                    .filter(course=order_item.course)\
                    .annotate(count_students=Count('curator_orders'))\
                    .order_by('curator_orders')\
                    .first()
                ConfirmedCourse.objects.create(user=user,
                                               course=order_item.course,
                                               coupon=order.coupon,
                                               price_with_discount=price_with_discount,
                                               create_date=date.today(),
                                               update_date=date.today(),
                                               end_date=end_date,
                                               curator=curator)
        return Response()
