# Generated by Django 3.1.7 on 2021-03-20 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('master', '0016_auto_20210320_1448'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fuel',
            name='Name',
            field=models.CharField(max_length=20, unique=True),
        ),
        migrations.AlterField(
            model_name='variant',
            name='Name',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]
