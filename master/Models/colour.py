from django.db import models

from .brand import Brand
from .model import Model
from .fuel import Fuel
from .variant import Variant


colour_type = (
    ('Pearl', 'Pearl'),
    ('Flat', 'Flat'),
)


class Colour(models.Model):
    Name = models.CharField(max_length=100)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    model = models.ForeignKey(Model, on_delete=models.CASCADE)
    fuel = models.ForeignKey(Fuel, on_delete=models.CASCADE)
    variant = models.ForeignKey(Variant, on_delete=models.CASCADE)
    typecode = models.CharField(max_length=20, choices=colour_type)

    def __str__(self):
        return f'{self.Name} / {self.typecode}'
