# Generated by Django 4.2.1 on 2023-06-15 18:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0002_remove_classnumber_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lesson',
            name='image',
        ),
    ]
