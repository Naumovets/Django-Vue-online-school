# Generated by Django 4.2.2 on 2023-07-23 17:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0011_fileofwebinar_title'),
    ]

    operations = [
        migrations.RenameField(
            model_name='curator',
            old_name='curator',
            new_name='user',
        ),
    ]
