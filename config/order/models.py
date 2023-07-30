from django.db import models

from cart.models import Coupon
from course.models import Course, Curator
from user.models import CustomUser


class ConfirmedCourse(models.Model):
    """
    Модель оплаченных курсов.
    Для одного и того же пользователя и курса не нужно добавлять новый объект, нужно обновить информацию
    update_date и end_date
    """

    user = models.ForeignKey(CustomUser,
                             on_delete=models.CASCADE,
                             verbose_name='Пользователь',
                             related_name='order_courses')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='Курс', related_name='order_courses')
    price_with_discount = models.DecimalField(verbose_name='Цена по скидке\n(если есть)',
                                              decimal_places=0,
                                              max_digits=9,
                                              null=True,
                                              blank=True)
    coupon = models.ForeignKey(Coupon, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Купон')
    create_date = models.DateField(verbose_name='Куплен')
    update_date = models.DateField(verbose_name='Продлен')
    end_date = models.DateField(verbose_name='Окончание')
    curator = models.ForeignKey(Curator,
                                on_delete=models.SET_NULL,
                                null=True,
                                blank=True,
                                verbose_name='Куратор',
                                related_name='curator_orders')

    def __str__(self):
        return str(self.user) + " " + str(self.course)

    class Meta:
        verbose_name = 'Купленный курс'
        verbose_name_plural = 'Купленные курсы'


class Order(models.Model):
    """
    Модель заказа.
    К ней привязаны курсы, которые хочет купить пользователь.
    """
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name='Пользователь', related_name='orders')
    coupon = models.ForeignKey(Coupon, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Купон')
    create_date = models.DateField(auto_now_add=True, verbose_name='Дата создания заказа')
    result_price = models.DecimalField(verbose_name='Полная цена',
                                     decimal_places=0,
                                     max_digits=9,
                                     null=True,
                                     blank=True)
    paid = models.BooleanField(default=False, verbose_name='Оплачен')

    def __str__(self):
        return str(self.user)

    class Meta:
        verbose_name = 'Заказ пользователя'
        verbose_name_plural = 'Заказы пользователей'


class OrderItem(models.Model):
    """
    Модель заказанного курса.
    """

    class Period(models.TextChoices):
        FULL = 'FL', 'Полный'
        MONTH = 'MN', 'Месячный'

    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True, related_name='items', verbose_name='Заказ')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='Курс', related_name='order_items')
    period = models.CharField(max_length=2, verbose_name='Период', choices=Period.choices)

    def __str__(self):
        return str(self.course)

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'
