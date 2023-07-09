# Generated by Django 4.2.2 on 2023-07-08 03:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('hotel_booking', '0001_initial'),
        ('booking', '0001_initial'),
        ('accounts', '0001_initial'),
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='reserved_products',
            field=models.ManyToManyField(related_name='reserved_users', through='booking.Book', to='hotel_booking.hotelproduct'),
        ),
        migrations.AddField(
            model_name='user',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions'),
        ),
    ]
