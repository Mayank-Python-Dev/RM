from django.db import models

from .brand import Brand


class Model(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    Name = models.CharField(max_length=20,unique=True)

    def __str__(self):
        return self.Name
