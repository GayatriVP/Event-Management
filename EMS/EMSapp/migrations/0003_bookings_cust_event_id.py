# Generated by Django 3.2.7 on 2021-11-21 12:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('EMSapp', '0002_bookings_events'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookings',
            name='cust_event_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='EMSapp.events'),
        ),
    ]