# Generated by Django 5.1.6 on 2025-03-06 05:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0003_alter_booking_endtime_alter_booking_ordertime_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='spaces',
            name='isBusy',
        ),
    ]
