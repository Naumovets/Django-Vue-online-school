from django.contrib import admin

from order.forms import ConfirmedCourseForm
from order.models import OrderItem, Order, ConfirmedCourse

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
    list_display = 'user', 'course', 'result_price', 'create_date', 'update_date', 'end_date', 'curator'
    form = ConfirmedCourseForm
