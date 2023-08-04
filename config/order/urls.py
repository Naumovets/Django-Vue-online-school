from django.urls import path

from cart.views import ExtendCourse
from order.views import addFreeCourseOrderItem, addOrderItems, ConfirmOrder

urlpatterns = [
    path('add_free_course/<int:course_id>', addFreeCourseOrderItem.as_view(), name='addFreeCourseOrderItem'),
    path('add_order_items/', addOrderItems.as_view(), name='add_order_items'),
    path('extend_course/', ExtendCourse.as_view(), name='extend_course'),
    path('add_order_items/<str:coupon_code>', addOrderItems.as_view(), name='confirm_order'),
    path('confirm_order/<int:order_id>', ConfirmOrder.as_view(), name='confirm_order'),
]