from django.db import models

from sales.models import *

from django import forms
from django.forms.fields import *

from django.contrib.admin.widgets import AdminDateWidget
from django.forms.fields import DateField

class CreatePayment(models.Model):
	BookingID = models.ForeignKey(Salesbooking,on_delete=models.CASCADE)
	Payment_Method = models.CharField(max_length=100)
	Amount = models.IntegerField()
	Date = models.DateField(auto_now_add=False)
	Total_Amount = models.IntegerField(null=True)
	Difference = models.IntegerField(null=True)

# class MyModelForm(forms.ModelForm):
#     Date = forms.DateField(widget=AdminDateWidget)

#     class Meta:
#         model = CreatePayment
#         fields = "__all__"