# Generated by Django 4.2.3 on 2023-07-18 02:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('hotel_booking', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('date', models.DateField(auto_now_add=True)),
                ('state', models.IntegerField(default=0)),
                ('phone', models.CharField(max_length=13)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='books', to='hotel_booking.hotelproduct')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='books', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
