# Generated by Django 3.1.7 on 2021-04-06 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0015_auto_20210406_1237'),
    ]

    operations = [
        migrations.AlterField(
            model_name='salesbooking',
            name='status',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
