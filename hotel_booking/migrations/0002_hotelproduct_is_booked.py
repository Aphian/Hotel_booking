# Generated by Django 4.2.3 on 2023-07-12 03:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel_booking', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotelproduct',
            name='is_booked',
            field=models.ImageField(default=0, upload_to=''),
        ),
    ]