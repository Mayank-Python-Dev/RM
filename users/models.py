from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models
from master.Models.dealership import Dealership


class CustomUser(AbstractUser):
    dealershipname = models.ForeignKey(
        Dealership, blank=True, null=True, on_delete=models.CASCADE)

    class Meta:
        db_table = 'auth_user'
