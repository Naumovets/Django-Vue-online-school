from django.contrib import admin

from order.forms import ConfirmedCourseForm
from order.models import OrderItem, Order, ConfirmedCourse
from user.models import CustomUser
#
#
# @admin.register(Order)
# class OrderAdmin(admin.ModelAdmin):
#     list_display = ('user',)
#     search_fields = ('user',)
#     inlines = [OrderItemInline]
#
#
# @admin.register(OrderItem)
# class OrderItemAdmin(admin.ModelAdmin):
#     list_display = ('course', 'curator', 'get_user', 'get_user_link', 'update_date', 'end_date', 'active')
#     list_filter = ('active', 'end_date', 'update_date')
#     search_fields = ('course', 'curator', 'get_user', 'get_user_link', 'active')
#
#     @admin.display(description='Пользователь')
#     def get_user(self, obj):
#         return obj.order.user
#
#     @admin.display(description='Ссылка')
#     def get_user_link(self, obj):
#         return obj.order.user.vk_link


class OrderItemInline(admin.StackedInline):
    model = OrderItem
    extra = 0


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'coupon', 'get_count_courses', 'create_date', 'result_price', 'paid')
    list_filter = ('id', 'user', 'coupon', 'create_date', 'result_price', 'paid')
    search_fields = ('id', 'create_date', 'result_price', 'paid')
    inlines = [OrderItemInline]

    @admin.display(description='Количество курсов')
    def get_count_courses(self, obj):
        return len(obj.items.all())


@admin.register(ConfirmedCourse)
class ConfirmedCourseAdmin(admin.ModelAdmin):
    list_display = 'user', 'course', 'price_with_discount', 'create_date', 'update_date', 'end_date', 'curator'
    form = ConfirmedCourseForm
