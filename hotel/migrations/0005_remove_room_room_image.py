# Generated by Django 3.2.16 on 2023-01-17 10:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0004_room_room_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='room',
            name='room_image',
        ),
    ]
