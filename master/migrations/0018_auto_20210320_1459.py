# Generated by Django 3.1.7 on 2021-03-20 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('master', '0017_auto_20210320_1450'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fuel',
            name='Name',
            field=models.CharField(choices=[('Petrol', 'Petrol'), ('Diesel', 'Diesel')], max_length=20),
        ),
    ]
