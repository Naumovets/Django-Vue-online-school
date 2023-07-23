import json

from django.core.exceptions import ObjectDoesNotExist
from rest_framework.response import Response
from rest_framework.views import APIView

from cart.models import CartItem, Cart
from cart.serializers import CartItemSerializer, CartItemForPriceSerializer
from cart.services.cart_manager import CartManager
from course.models import Course


class CartView(APIView):

    def get(self, request):
        user = request.user
        cart_items = CartItem.objects.filter(cart__user=user)
        cart_items_serialized = CartItemSerializer(cart_items, many=True)
        return Response(cart_items_serialized.data)

    def post(self, request):
        user = request.user
        try:
            cart = Cart.objects.get(user=user)
        except ObjectDoesNotExist:
            cart = Cart()
            cart.user = user
            cart.save()
        try:
            course = Course.objects.get(id=request.POST.get('id'))
        except ObjectDoesNotExist:
            return Response({'error': 'данного курса не существует'})

        if CartItem.objects.filter(course=course, cart=cart).exists():
            return Response({'error': 'Данный курс уже добавлен в корзину'})

        CartItem.objects.create(cart=cart, course=course)
        return Response()

    def delete(self, request, id):
        user = request.user
        try:
            cart = Cart.objects.get(user=user)
        except ObjectDoesNotExist:
            cart = Cart()
            cart.user = user
            cart.save()
            return Response({'error': 'данного курса нет в корзине'})
        try:
            course = Course.objects.get(id=id)
        except ObjectDoesNotExist:
            return Response({'error': 'данного курса не существует'})

        if CartItem.objects.filter(course=course, cart=cart).exists():
            cart_item = CartItem.objects.get(course=course, cart=cart)
            cart_item.delete()
        else:
            return Response({'error': 'данного курса нет в корзине'})

        return Response()


class PriceCartItemView(APIView):

    def post(self, request):
        coupon_code = request.GET.get('coupon_code', None)
        user = request.user
        json_parsed = json.loads(request.body)
        data_of_period_of_paying_courses = CartItemForPriceSerializer(data=json_parsed, many=True)
        data_of_period_of_paying_courses.is_valid()
        total_price = CartManager.get_total_price(user, coupon_code, data_of_period_of_paying_courses.validated_data)
        return Response(total_price)
