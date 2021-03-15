from django.contrib import admin

#Register your models here.
from .models import *


admin.site.register(Brand)
admin.site.register(Model)
admin.site.register(Fuel)
admin.site.register(Variant)
admin.site.register(Colour)