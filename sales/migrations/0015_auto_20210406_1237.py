# Generated by Django 3.1.7 on 2021-04-06 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0014_auto_20210406_1223'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='salesbooking',
            name='Status',
        ),
        migrations.AddField(
            model_name='salesbooking',
            name='status',
            field=models.CharField(default=0, max_length=50),
            preserve_default=False,
        ),
    ]