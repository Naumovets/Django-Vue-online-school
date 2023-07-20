from django.db import models

from course.models import Course
from user.models import CustomUser


class Coupon(models.Model):
    code = models.CharField(max_length=20, verbose_name='Промокод')
    discount = models.IntegerField(verbose_name='Процент скидки')

    def __str__(self):
        return "Промокод: " + self.code

    class Meta:
        verbose_name = 'Промокод'
        verbose_name_plural = 'Промокоды'


class UsedCoupon(models.Model):
    coupon = models.ForeignKey(Coupon, on_delete=models.CASCADE, verbose_name='Купон')
    user = models.ForeignKey(CustomUser,
                             on_delete=models.CASCADE,
                             verbose_name='Пользователь',
                             related_name='user_coupon')

    def __str__(self):
        return str(self.coupon) + " использован " + str(self.user)

    class Meta:
        verbose_name = 'Использованный промокод'
        verbose_name_plural = 'Использованные промокоды'


class Cart(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name='Пользователь', related_name='cart')

    def __str__(self):
        return 'Корзина пользователя ' + str(self.user)

    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзины'


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, verbose_name='Корзина', related_name='items')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='Курс')

    def __str__(self):
        return str(self.course) + ' для ' + str(self.cart.user)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
