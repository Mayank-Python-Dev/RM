# Generated by Django 3.1.7 on 2021-03-23 05:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0006_salesbooking_booking_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='salesbooking',
            name='booking_receipt',
        ),
        migrations.RemoveField(
            model_name='salesbooking',
            name='order_form',
        ),
        migrations.RemoveField(
            model_name='salesbooking',
            name='quotation',
        ),
    ]
