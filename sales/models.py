from django.db import models

# Create your models here.

from master.Models.dealbreakup import Dealbreakup

from master.Models.brand import *

from master.Models.colour import *

from master.Models.variant import *

from master.Models.fuel import *

from master.Models.model import *

from master.Models.dealership import *

from django.contrib.auth.models import User, Group


def user_directory_path(instance, filename):
    return '{0}/{1}'.format(instance.booking_ID, filename)


class Salesbooking(models.Model):
    booking_ID = models.CharField(max_length=20)
    customer_name = models.CharField(max_length=50)
    contact_number = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    Brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    Model = models.ForeignKey(Model, on_delete=models.CASCADE,)
    Variant = models.ForeignKey(Variant, on_delete=models.CASCADE)
    Colour = models.ForeignKey(Colour, on_delete=models.CASCADE)
    Date = models.DateTimeField(auto_now_add=True)
    Ex_Showroom_Price = models.FloatField()
    Insurance_AMT = models.FloatField()
    RTO = models.FloatField()
    FASTAG = models.FloatField()
    TCS = models.FloatField()
    TOTAL = models.FloatField()
    ACC = models.FloatField()
    Extended_Warranty = models.FloatField()
    Annual_Maintanence_Cost = models.FloatField()
    On_Road_Price = models.FloatField()
    booking_receipt = models.FileField(
        null=True, blank=True, upload_to=user_directory_path)
    quotation = models.FileField(
        null=True, blank=True, upload_to=user_directory_path)
    order_form = models.FileField(
        null=True, blank=True, upload_to=user_directory_path)
    Delivery_Order = models.FileField(
        null=True, blank=True, upload_to=user_directory_path)
    Consumer_offer = models.FloatField(default=0)
    Exchange_bonus = models.FloatField(default=0)
    Corporate_discount = models.FloatField(default=0)
    Remarks = models.CharField(max_length=50)
    Dealer_discount = models.FloatField(default=0)
    Total_discount = models.FloatField(default=0)
    Down_Payment = models.FloatField(null=True, blank=True)
    Finance = models.FloatField(null=True, blank=True)
    Used_car = models.FloatField(null=True, blank=True)
    Total_Payment = models.FloatField(null=True, blank=True)
    status = models.CharField(
        max_length=50, null=True, blank=True)
    Modification = models.TextField(
        max_length=500, help_text='Write if you want to modify something!', blank=True)

    def __str__(self):
        return self.customer_name

    def getDict(self):
        return vars(self)
