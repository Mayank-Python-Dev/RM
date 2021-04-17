from django.db import models

from .brand import Brand
from .model import Model


class Fuel(models.Model):
    Name = models.CharField(max_length=100)

    def __str__(self):
        return self.Name
