# Generated by Django 4.2.2 on 2023-07-10 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_customuser_image_alter_customuser_last_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='users/', verbose_name='Фотография профиля'),
        ),
    ]
