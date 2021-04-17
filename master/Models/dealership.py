from django.db import models
# from django.contrib.auth.models import AbstractUser

# from django.contrib.auth.models import User


class Dealership(models.Model):
    # Account = models.OneToOneField(User, on_delete=models.CASCADE)
    Name = models.CharField(max_length=100)
    address = models.TextField()
    state = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    pincode = models.IntegerField()

    def __str__(self):
        return f'{self.Name}'


# class CustomUser(AbstractUser):
# 	Dealership = models.ForeignKey(Dealership,on_delete= models.CASCADE)


# 	def __str__(self):
# 		return f"{self.Dealership} : {self.username}"
