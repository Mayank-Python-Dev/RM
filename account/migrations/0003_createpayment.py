# Generated by Django 3.1.7 on 2021-04-26 19:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('sales', '0001_initial'),
        ('account', '0002_delete_paymentbreakup'),
    ]

    operations = [
        migrations.CreateModel(
            name='CreatePayment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Payment_Method', models.CharField(max_length=100)),
                ('Amount', models.IntegerField()),
                ('Date', models.DateField()),
                ('BookingID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sales.salesbooking')),
            ],
        ),
    ]