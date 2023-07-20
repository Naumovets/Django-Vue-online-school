from django.contrib import admin

from order.forms import OrderItemForm
from order.models import OrderItem, Order


class OrderItemInline(admin.StackedInline):
    model = OrderItem
    form = OrderItemForm
    extra = 1


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('user',)
    search_fields = ('user',)
    inlines = [OrderItemInline]


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('course', 'curator', 'get_user', 'get_user_link', 'update_date', 'end_date', 'active')
    list_filter = ('active', 'end_date', 'update_date')
    search_fields = ('course', 'curator', 'get_user', 'get_user_link', 'active')

    @admin.display(description='Пользователь')
    def get_user(self, obj):
        return obj.order.user

    @admin.display(description='Ссылка')
    def get_user_link(self, obj):
        return obj.order.user.vk_link
