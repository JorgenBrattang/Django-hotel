# Generated by Django 3.2.16 on 2023-01-11 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField()),
                ('catergory', models.CharField(choices=[('YAC', 'AC'), ('NAC', 'NO-AC'), ('LUX', 'LUXURY'), ('KIN', 'KING'), ('QEE', 'QUEEN')], max_length=3)),
                ('beds', models.IntegerField()),
                ('capacity', models.IntegerField()),
            ],
        ),
    ]