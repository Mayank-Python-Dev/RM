from django.db import models

from sales.models import *


class CreatePayment(models.Model):
	BookingID = models.ForeignKey(Salesbooking,on_delete=models.CASCADE)
	Payment_Method = models.CharField(max_length=100)
	Amount = models.IntegerField()
	Date = models.DateField(auto_now_add=False,null=True)