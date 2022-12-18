# Generated by Django 3.2.2 on 2022-12-17 08:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='PaymentHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('owner_id', models.IntegerField()),
                ('Place_name', models.CharField(max_length=100)),
                ('Room_House_No', models.CharField(max_length=100)),
                ('booker_id', models.IntegerField()),
                ('booker_name', models.CharField(max_length=100)),
                ('owner_name', models.CharField(max_length=100)),
                ('c_type', models.CharField(max_length=100)),
                ('amount', models.IntegerField()),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
                ('booking_date', models.DateTimeField(auto_now_add=True)),
                ('superuser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]