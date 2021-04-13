from .brand import Brand
from .model import Model
from .fuel import Fuel
from .variant import Variant
from .colour import Colour
from django.db import models

transmission_name = (
    ('Manual', 'Manual'),
    ('Automatic', 'Automatic'),
)


class Dealbreakup(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    model = models.ForeignKey(Model, on_delete=models.CASCADE)
    fuel = models.ForeignKey(Fuel, on_delete=models.CASCADE)
    variant = models.ForeignKey(Variant, on_delete=models.CASCADE)
    colour = models.ForeignKey(Colour, on_delete=models.CASCADE)
    transmission = models.CharField(max_length=20, choices=transmission_name)
    ex_Showroom_Price = models.FloatField()
    Insurance_Amount = models.FloatField()
    RTO = models.FloatField()
    FASTAG = models.FloatField()
    TCS = models.FloatField()
    TOTAL = models.FloatField()
    ACC = models.FloatField()
    extended_Warranty = models.FloatField()
    Annual_Maintanence_Cost = models.FloatField()
    on_Road_Price = models.FloatField()
    consume_offer = models.FloatField(default=0)
    exchange_bonus = models.FloatField(default=0)
    corporate_discount = models.FloatField(default=0)
    remarks = models.CharField(max_length=50)
    dealer_discount = models.FloatField(default=0)
    total_discount = models.FloatField(default=0)

    def __str__(self):
        return f'{self.model} Pricelist'
