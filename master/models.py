# from django.db import models

# # Create your models here.

# class Brand(models.Model):
#     Name = models.CharField(max_length=20)

#     def __str__(self):
#         return self.Name


# class Model(models.Model):
#     brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
#     Name = models.CharField(max_length=20)

#     def __str__(self):
#         return self.Name


# fueltype = (
#     ('Petrol', 'Petrol'),
#     ('Diesel', 'Diesel')
# )


# class Fuel(models.Model):
#     Name = models.CharField(max_length=20, choices=fueltype)
#     brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
#     model = models.ForeignKey(Model, on_delete=models.CASCADE)

#     def __str__(self):
#         return self.Name


# transmission_name = (
#     ('Manual', 'Manual'),
#     ('Automatic', 'Automatic'),
# )


# class Variant(models.Model):
#     Name = models.CharField(max_length=20)
#     brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
#     model = models.ForeignKey(Model, on_delete=models.CASCADE)
#     fuel = models.ForeignKey(Fuel, on_delete=models.CASCADE)
    

#     def __str__(self):
#         return self.Name


# colour_type = (
#     ('Pearl', 'Pearl'),
#     ('Flat', 'Flat'),
# )


# class Colour(models.Model):
#     Name = models.CharField(max_length=20)
#     brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
#     model = models.ForeignKey(Model, on_delete=models.CASCADE)
#     fuel = models.ForeignKey(Fuel, on_delete=models.CASCADE)
#     variant = models.ForeignKey(Variant, on_delete=models.CASCADE)
#     transmission = models.CharField(max_length=20, choices=transmission_name)
#     typecode = models.CharField(max_length=20, choices=colour_type)


#     def __str__(self):
#         return self.Name


# class Price