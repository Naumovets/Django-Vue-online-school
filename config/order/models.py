from django.db import models

from cart.models import Coupon
from course.models import Course
from user.models import CustomUser


class Order(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name='Пользователь', related_name='order')

    def __str__(self):
        return str(self.user)

    class Meta:
        verbose_name = 'Заказ пользователя'
        verbose_name_plural = 'Заказы пользователей'


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True, related_name='items', verbose_name='Заказ')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='Курс', related_name='orders')
    price_with_discount = models.DecimalField(verbose_name='Цена со скидкой',
                                              decimal_places=0,
                                              max_digits=9,
                                              null=True,
                                              blank=True)
    coupon = models.ForeignKey(Coupon, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Купон')
    create_date = models.DateField(verbose_name='Куплен')
    update_date = models.DateField(verbose_name='Продлен')
    end_date = models.DateField(verbose_name='Окончание')
    curator = models.ForeignKey(CustomUser,
                                on_delete=models.SET_NULL,
                                null=True,
                                verbose_name='Куратор',
                                related_name='curator_orders')
    active = models.BooleanField(default=False, verbose_name='Активный')

    def __str__(self):
        return str(self.order) + " " + str(self.course)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
