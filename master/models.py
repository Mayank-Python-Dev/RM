from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models
from django.utils.translation import gettext_lazy as _
# from django_countries.fields import CountryField

from .Models.dealership import Dealership

# class CustomUser(AbstractUser):
#     dealership = models.ForeignKey(Dealership,on_delete = models.CASCADE)
#     class Meta:
#         ordering = ['last_name']

#     def __str__(self):
#         return f"{self.username}: {self.first_name} {self.last_name}"