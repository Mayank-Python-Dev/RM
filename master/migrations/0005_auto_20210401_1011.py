# Generated by Django 3.1.7 on 2021-04-01 04:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('master', '0004_auto_20210331_1817'),
    ]

    operations = [
        migrations.RenameField(
            model_name='model',
            old_name='Name',
            new_name='Model',
        ),
    ]
