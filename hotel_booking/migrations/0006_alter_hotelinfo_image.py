# Generated by Django 4.2.3 on 2023-07-12 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel_booking', '0005_alter_hotelinfo_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotelinfo',
            name='image',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
    ]
