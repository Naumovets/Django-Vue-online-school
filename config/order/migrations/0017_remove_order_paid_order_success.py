# Generated by Django 4.2.2 on 2023-08-06 02:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0016_alter_order_payment_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='paid',
        ),
        migrations.AddField(
            model_name='order',
            name='success',
            field=models.BooleanField(default=False, verbose_name='Успешно'),
        ),
    ]