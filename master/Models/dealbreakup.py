from django.db import models

from .brand import Brand
from .model import Model
from .fuel import Fuel
from .variant import Variant
from .colour import Colour




transmission_name = (
    ('Manual', 'Manual'),
    ('Automatic', 'Automatic'),
)



class Dealbreakup(models.Model):
	brand = models.ForeignKey(Brand,on_delete = models.CASCADE)
	model = models.ForeignKey(Model,on_delete = models.CASCADE)
	fuel = models.ForeignKey(Fuel,on_delete = models.CASCADE)
	variant = models.ForeignKey(Variant,on_delete = models.CASCADE)
	colour = models.ForeignKey(Colour,on_delete = models.CASCADE)
	transmission = models.CharField(max_length=20, choices=transmission_name)
	ex_Showroom_Price = models.FloatField()
	ins_AMT = models.FloatField()
	rto = models.FloatField()
	fASTag = models.FloatField()
	tcs = models.FloatField()
	total = models.FloatField()
	acc = models.FloatField()
	extended_Warranty = models.FloatField()
	amc = models.FloatField()
	on_Road_Price = models.FloatField()

	def __str__(self):
		return f'{self.model} Pricelist'

