from django.db import models

from .brand import Brand
from .model import Model
from .fuel import Fuel


class Variant(models.Model):
    Name = models.CharField(max_length=20)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    model = models.ForeignKey(Model, on_delete=models.CASCADE)
    fuel = models.ForeignKey(Fuel, on_delete=models.CASCADE)

    def __str__(self):
        return self.Name
