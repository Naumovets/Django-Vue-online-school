from django.urls import path

from cart.views import CartView, PriceCartItemView

urlpatterns = [
    path('cart', CartView.as_view(), name='cart'),
    path('cart/<int:id>', CartView.as_view(), name='cart_delete'),
    path('price_cart_item', PriceCartItemView.as_view(), name='price')
]
