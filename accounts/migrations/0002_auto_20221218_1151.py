# Generated by Django 3.2.2 on 2022-12-18 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='useraccount',
            name='DOB',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='useraccount',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='account'),
        ),
        migrations.AddField(
            model_name='useraccount',
            name='staff',
            field=models.BooleanField(default=False),
        ),
    ]