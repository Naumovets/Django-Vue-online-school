# Generated by Django 4.2.2 on 2023-07-15 19:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cart',
            options={'verbose_name': 'Корзина', 'verbose_name_plural': 'Корзины'},
        ),
        migrations.AlterModelOptions(
            name='cartitem',
            options={'verbose_name': 'Товар', 'verbose_name_plural': 'Товары'},
        ),
        migrations.AlterModelOptions(
            name='coupon',
            options={'verbose_name': 'Промокод', 'verbose_name_plural': 'Промокоды'},
        ),
        migrations.AlterModelOptions(
            name='usedcoupon',
            options={'verbose_name': 'Использованный промокод', 'verbose_name_plural': 'Использованные промокоды'},
        ),
    ]
