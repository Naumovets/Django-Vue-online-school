# Generated by Django 4.2.2 on 2023-07-23 16:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('order', '0008_alter_order_options_alter_orderitem_options_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='full_price',
            new_name='result_price',
        ),
        migrations.AlterField(
            model_name='ordercourse',
            name='curator',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='curator_orders', to=settings.AUTH_USER_MODEL, verbose_name='Куратор'),
        ),
    ]