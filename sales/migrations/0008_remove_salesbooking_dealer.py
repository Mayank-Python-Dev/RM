# Generated by Django 3.1.7 on 2021-03-31 12:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0007_auto_20210331_1806'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='salesbooking',
            name='Dealer',
        ),
    ]