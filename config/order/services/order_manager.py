import decimal

from cart.models import Coupon
from course.models import Course
from order.models import OrderItem


class OrderManager:

    @staticmethod
    def get_result_price(course: Course, coupon: Coupon, period: str, many=False) -> int:
        if not course.price:
            return 0
        discount = coupon.discount if coupon else 0
        if many:
            discount += 15
        coef_price_with_discount = decimal.Decimal((100 - discount) / 100)
        return course.price * coef_price_with_discount \
            if period == OrderItem.Period.MONTH \
            else course.full_price * coef_price_with_discount
