import decimal

from cart.models import Coupon
from course.models import Course


class OrderManager:

    @staticmethod
    def get_price_with_discount(course: Course, coupon: Coupon, many=False) -> int:
        if not course.price:
            return 0
        discount = coupon.discount if coupon else 0
        if many:
            discount += 15
        coef_price_with_discount = decimal.Decimal((100 - discount) / 100)
        return course.price * coef_price_with_discount
