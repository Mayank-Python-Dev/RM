# Generated by Django 3.1.7 on 2021-03-19 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0003_salesbooking_brand'),
    ]

    operations = [
        migrations.AlterField(
            model_name='salesbooking',
            name='email',
            field=models.EmailField(max_length=50),
        ),
    ]