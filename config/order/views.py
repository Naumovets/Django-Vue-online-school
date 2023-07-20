from django.shortcuts import render
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import permission_classes, authentication_classes
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from order.models import Order, OrderItem
from order.serializers import OrderItemSerializer


@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
class OrderItemsView(APIView):

    def get(self, request):
        user = request.user
        if Order.objects.filter(user=user).exists():
            order = Order.objects.get(user=user)
            order_items = order.items.all()
            order_items_serialized = OrderItemSerializer(order_items, many=True)
            return Response(order_items_serialized.data)
        else:
            return Response({'response': 'Курсов нет'})


@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
class OrderItemView(APIView):

    def get(self, request, slug):
        user = request.user
        order = get_object_or_404(Order,
                                  user=user)
        order_item = get_object_or_404(OrderItem,
                                       order=order,
                                       course__slug=slug)
        order_items_serialized = OrderItemSerializer(order_item)
        return Response(order_items_serialized.data)