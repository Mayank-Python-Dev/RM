# Generated by Django 3.1.7 on 2021-03-18 06:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('master', '0007_auto_20210316_1138'),
    ]

    operations = [
        migrations.CreateModel(
            name='Salesbooking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('booking_receipt', models.CharField(max_length=20)),
                ('customer_name', models.CharField(max_length=50)),
                ('contact_number', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=20)),
                ('Date', models.DateTimeField(auto_now_add=True)),
                ('Acc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='salesbooking_create_acc', to='master.dealbreakup')),
                ('Amc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='salesbooking_create_amc', to='master.dealbreakup')),
                ('Colour', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='salesbooking_create_colour', to='master.dealbreakup')),
                ('Ex_Showroom_Price', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='salesbooking_create_price', to='master.dealbreakup')),
                ('Extended_Warranty', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='salesbooking_create_ew', to='master.dealbreakup')),
                ('FASTag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='salesbooking_create_fastag', to='master.dealbreakup')),
                ('Ins_AMT', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='salesbooking_create_amt', to='master.dealbreakup')),
                ('Model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='salesbooking_create_model', to='master.dealbreakup')),
                ('On_Road_Price', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='salesbooking_create_onroadprice', to='master.dealbreakup')),
                ('Rto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='salesbooking_create_rto', to='master.dealbreakup')),
                ('Tcs', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='salesbooking_create_tcs', to='master.dealbreakup')),
                ('Total', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='salesbooking_create_total', to='master.dealbreakup')),
                ('Variant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='salesbooking_create_variant', to='master.dealbreakup')),
            ],
        ),
    ]
