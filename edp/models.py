from django.db import models

# Create your models here.

from sales.models import *


class Uploadfile(models.Model):
	ID = models.ForeignKey(Salesbooking,on_delete = models.CASCADE,null = True)
	DMS = models.FileField()
	Tally = models.FileField()

	def __str__(self):
		return str(self.ID.customer_name)
