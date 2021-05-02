from django.db import models

# Create your models here.

from sales.models import *


def user_directory_path(instance, filename):
    return '{0}/{1}'.format(instance.ID, filename)

class Uploadfile(models.Model):
	ID = models.ForeignKey(Salesbooking,on_delete = models.CASCADE,null = True)
	DMS = models.FileField(null = True, blank=True, upload_to=user_directory_path)
	Tally = models.FileField(null = True, blank=True, upload_to=user_directory_path)
	RTO = models.FileField(null=True, blank=True, upload_to=user_directory_path)
	DMS_Tally_Status = models.CharField(max_length = 100) 
	Insurance = models.FileField(null=True, blank=True, upload_to=user_directory_path)

	def __str__(self):
		return str(self.ID.customer_name)


