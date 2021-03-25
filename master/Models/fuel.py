from django.db import models

from .brand import Brand
from .model import Model


fueltype = (
	('Petrol','Petrol'),
	('Diesel','Diesel'),
	)

class Fuel(models.Model):
    Name = models.CharField(max_length=20,choices = fueltype , unique = True)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    model = models.ForeignKey(Model, on_delete=models.CASCADE)

    def __str__(self):
        return self.Name
