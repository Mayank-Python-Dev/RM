# Generated by Django 3.1.7 on 2021-04-21 05:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('master', '0014_auto_20210415_1151'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dealbreakup',
            old_name='ACC',
            new_name='ACCESSORIES',
        ),
        migrations.RemoveField(
            model_name='dealbreakup',
            name='TOTAL',
        ),
    ]
