# Generated by Django 5.1.6 on 2025-03-04 16:20

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Accomodation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256)),
                ('rating', models.IntegerField(blank=True, null=True)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('accomodation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookings.accomodation')),
            ],
        ),
        migrations.CreateModel(
            name='Spaces',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('capacity', models.IntegerField(blank=True, null=True)),
                ('isBusy', models.BooleanField()),
                ('accomodation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookings.accomodation')),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('confirmed', 'Confirmed'), ('cancelled', 'Cancelled')], default='pending', max_length=20)),
                ('orderTime', models.DateField(auto_now_add=True)),
                ('startTime', models.DateField()),
                ('endTime', models.DateField()),
                ('accomodation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookings.accomodation')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('space', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookings.spaces')),
            ],
        ),
    ]
