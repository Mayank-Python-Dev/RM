# Generated by Django 3.1.7 on 2021-04-30 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_auto_20210430_1212'),
    ]

    operations = [
        migrations.AddField(
            model_name='createpayment',
            name='Difference',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='createpayment',
            name='Total_Amount',
            field=models.IntegerField(null=True),
        ),
        migrations.DeleteModel(
            name='TotalPayment',
        ),
    ]