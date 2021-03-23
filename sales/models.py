from django.db import models

# Create your models here.


from master.Models.dealbreakup import Dealbreakup

from master.Models.brand import *

from master.Models.colour import *

from master.Models.variant import *

from master.Models.fuel import *

from master.Models.model import *

from django.contrib.auth.models import User ,Group

def user_directory_path(instance, filename):
    return '{0}/{1}'.format(instance.customer_name, filename)

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
    Ins_AMT = models.FloatField()
    Rto = models.FloatField()
    FASTag = models.FloatField()
    Tcs = models.FloatField()
    Total = models.FloatField()
    Acc = models.FloatField()
    Extended_Warranty = models.FloatField()
    Amc = models.FloatField()
    On_Road_Price = models.FloatField()
    booking_receipt = models.FileField(
        null=True, blank=True, upload_to=user_directory_path)
    quotation = models.FileField(null=True, blank=True, upload_to=user_directory_path)
    order_form = models.FileField(
        null=True, blank=True, upload_to=user_directory_path)



    # def getDict(self):
    #     return vars(self)
    class Meta:
        ordering = ['customer_name']
        def __str__(self):
            return f"{self.customer_name}"