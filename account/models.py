from django.db import models

from sales.models import *


class PaymentBreakUP(models.Model):
    ID = models.ForeignKey(Salesbooking,on_delete=models.CASCADE,null=True)
    Payment_Method = models.CharField(max_length=100)
    payment = models.IntegerField()
