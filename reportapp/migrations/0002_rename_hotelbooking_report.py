# Generated by Django 3.2.2 on 2022-12-18 05:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reportapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='HotelBooking',
            new_name='Report',
        ),
    ]