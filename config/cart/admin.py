from django.contrib import admin

from cart.models import Cart, CartItem, Coupon, UsedCoupon


class CartItemInline(admin.StackedInline):
    model = CartItem
    extra = 1


@admin.register(Cart)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ('user', )
    inlines = [CartItemInline, ]
    search_fields = ('user', )


admin.site.register(Coupon)
admin.site.register(UsedCoupon)
