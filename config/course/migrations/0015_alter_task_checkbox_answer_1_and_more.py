# Generated by Django 4.2.2 on 2023-08-06 21:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0014_alter_task_checkbox_answer_1_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='checkbox_answer_1',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Множественный ответ 1'),
        ),
        migrations.AlterField(
            model_name='task',
            name='checkbox_answer_2',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Множественный ответ 2'),
        ),
        migrations.AlterField(
            model_name='task',
            name='checkbox_answer_3',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Множественный ответ 3'),
        ),
        migrations.AlterField(
            model_name='task',
            name='checkbox_answer_4',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Множественный ответ 4'),
        ),
        migrations.AlterField(
            model_name='task',
            name='checkbox_answer_5',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Множественный ответ 5'),
        ),
    ]
