# Generated by Django 4.2.2 on 2023-07-22 20:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0011_fileofwebinar_title'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cart', '0002_alter_cart_options_alter_cartitem_options_and_more'),
        ('order', '0007_alter_orderitem_active'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'verbose_name': 'Курсы пользователя', 'verbose_name_plural': 'Курсы пользователей'},
        ),
        migrations.AlterModelOptions(
            name='orderitem',
            options={'verbose_name': 'Заказы пользователей'},
        ),
        migrations.RemoveField(
            model_name='orderitem',
            name='active',
        ),
        migrations.RemoveField(
            model_name='orderitem',
            name='coupon',
        ),
        migrations.RemoveField(
            model_name='orderitem',
            name='create_date',
        ),
        migrations.RemoveField(
            model_name='orderitem',
            name='curator',
        ),
        migrations.RemoveField(
            model_name='orderitem',
            name='end_date',
        ),
        migrations.RemoveField(
            model_name='orderitem',
            name='price_with_discount',
        ),
        migrations.RemoveField(
            model_name='orderitem',
            name='update_date',
        ),
        migrations.AddField(
            model_name='order',
            name='coupon',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='cart.coupon', verbose_name='Купон'),
        ),
        migrations.AddField(
            model_name='order',
            name='create_date',
            field=models.DateField(auto_now_add=True, default=None, verbose_name='Дата создания заказа'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='full_price',
            field=models.DecimalField(blank=True, decimal_places=0, max_digits=9, null=True, verbose_name='Полная цена'),
        ),
        migrations.AddField(
            model_name='order',
            name='paid',
            field=models.BooleanField(default=False, verbose_name='Оплачен'),
        ),
        migrations.AddField(
            model_name='orderitem',
            name='period',
            field=models.CharField(default=None, max_length=5, verbose_name='Период'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='order',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_items', to='course.course', verbose_name='Курс'),
        ),
        migrations.CreateModel(
            name='OrderCourse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price_with_discount', models.DecimalField(blank=True, decimal_places=0, max_digits=9, null=True, verbose_name='Цена со скидкой')),
                ('create_date', models.DateField(verbose_name='Куплен')),
                ('update_date', models.DateField(verbose_name='Продлен')),
                ('end_date', models.DateField(verbose_name='Окончание')),
                ('coupon', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='cart.coupon', verbose_name='Купон')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_courses', to='course.course', verbose_name='Курс')),
                ('curator', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='curator_orders', to=settings.AUTH_USER_MODEL, verbose_name='Куратор')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_courses', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Товары',
            },
        ),
    ]
