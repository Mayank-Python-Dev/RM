from django.contrib import admin

from .models import *
# Register your models here.


@admin.register(PaymentBreakUP)
class BookingPayment(admin.ModelAdmin):
    list_display = ['ID', 'Payment_Method', 'payment']
