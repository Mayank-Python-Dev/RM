# Generated by Django 3.1.7 on 2021-03-31 12:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0006_auto_20210331_1720'),
    ]

    operations = [
        migrations.RenameField(
            model_name='salesbooking',
            old_name='Dealership',
            new_name='Dealer',
        ),
    ]
