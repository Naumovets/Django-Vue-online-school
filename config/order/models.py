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
    result_price = models.DecimalField(verbose_name='Итоговая цена',
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
    token = models.TextField(verbose_name='Токен (См. Подпись запроса)', blank=True, null=True)
    exp_date = models.TextField(verbose_name='Срок действия карты MMYY', blank=True, null=True)
    pan = models.TextField(verbose_name='Замаскированный номер карты/Замаскированный номер телефона', blank=True,
                           null=True)
    card_id = models.IntegerField(verbose_name='Идентификатор сохраненной карты в системе банка', blank=True, null=True)
    amount = models.DecimalField(decimal_places=0, max_digits=10, verbose_name='Оплачено в коп.', blank=True, null=True)
    error_code = models.CharField(max_length=20, verbose_name='Код ошибки (0=Успех)', blank=True, null=True)
    payment_id = models.BigIntegerField(verbose_name='Идентификатор платежа в системе банка', null=True, blank=True)
    status = models.CharField(max_length=20, verbose_name='Статус', null=True, blank=True)
    terminal_key = models.TextField(null=True, blank=True)

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
    result_price = models.DecimalField(verbose_name='Полная цена',
                                       decimal_places=0,
                                       max_digits=9,
                                       null=True,
                                       blank=True)

    def __str__(self):
        return str(self.course)

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'
