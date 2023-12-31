# Generated by Django 4.2.2 on 2023-07-11 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0002_alter_course_options_alter_exam_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='curator',
        ),
        migrations.AlterField(
            model_name='course',
            name='description',
            field=models.TextField(verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='course',
            name='status',
            field=models.CharField(choices=[('MN', 'Основной'), ('SP', 'Спецкурс'), ('FR', 'Бесплатный')], default='MN', max_length=2, verbose_name='Тип курса'),
        ),
    ]
