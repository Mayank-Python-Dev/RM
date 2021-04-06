# Generated by Django 3.1.7 on 2021-04-06 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0012_salesbooking_total_payment'),
    ]

    operations = [
        migrations.AddField(
            model_name='salesbooking',
            name='Status',
            field=models.CharField(choices=[('Approved', 'Approved'), ('Rejected', 'Rejected')], default='Rejected', max_length=50, null=True),
        ),
    ]