from django.core.exceptions import ObjectDoesNotExist

from cart.models import Coupon, UsedCoupon
from course.models import Course
from user.models import CustomUser


class PriceManager:

    @staticmethod
    def get_total_price(user: CustomUser, coupon_code: str = None, data_of_courses: list = None) -> dict:
        """ Вывод итоговой цены """

        price = 0
        discount = 0
        response = None
        error = None

        for data in data_of_courses:
            course = Course.objects.get(id=data['id'])
            if data['period'] == 'month':
                price += course.price
            else:
                price += course.full_price

        if len(data_of_courses) > 1:
            discount += 15

        if coupon_code:
            try:
                coupon = Coupon.objects.get(code=coupon_code)
                if not UsedCoupon.objects.filter(coupon=coupon, user=user).exists():
                    discount += coupon.discount
                else:
                    error = f'Вы уже использовали купон: {coupon_code}'
            except ObjectDoesNotExist:
                error = 'Данного купона не существует'

        # cart_items = user.cart.get().items.all()
        # for item in cart_items:
        #     price += item.course.price if item.course.price else 0
        #
        # if len(cart_items) > 1:
        #     discount += 15
        #
        #
        if discount > 0:
            response = f'Скидка {discount}%'
        price_with_discount = int(price * (100 - discount)/100)

        result = {'price': price,
                  'discount': discount,
                  'price_with_discount': price_with_discount,
                  'response': response,
                  'error': error}

        return result


