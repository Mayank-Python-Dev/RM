from django.contrib import admin

from .models import *
# Register your models here.


@admin.register(CreatePayment)
class Createpayment(admin.ModelAdmin):
    list_display = ['BookingID', 'Payment_Method', 'Amount','Date']
