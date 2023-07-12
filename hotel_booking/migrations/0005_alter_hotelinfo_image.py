# Generated by Django 4.2.3 on 2023-07-12 05:53

from django.db import migrations
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('hotel_booking', '0004_alter_hotelinfo_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotelinfo',
            name='image',
            field=imagekit.models.fields.ProcessedImageField(upload_to='images/'),
        ),
    ]