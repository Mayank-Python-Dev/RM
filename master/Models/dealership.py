from django.db import models
from django.contrib.auth.models import AbstractUser


class Dealership(models.Model):
	Name = models.CharField(max_length = 50, unique = True)
	address = models.CharField(max_length = 50)
	state = models.CharField(max_length = 50)
	city = models.CharField(max_length = 50)
	pincode = models.IntegerField()


	def __str__(self):
		return self.Name


# class CustomUser(AbstractUser):
# 	Dealership = models.ForeignKey(Dealership,on_delete= models.CASCADE)


# 	def __str__(self):
# 		return f"{self.Dealership} : {self.username}"