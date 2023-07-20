from django.urls import path

from order.views import OrderItemsView, OrderItemView

urlpatterns = [
    path('', OrderItemsView.as_view(), name='orders'),
    path('<slug:slug>', OrderItemView.as_view(), name='orderItem')
]