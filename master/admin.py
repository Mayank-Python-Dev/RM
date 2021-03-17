from django.contrib import admin

#Register your models here.
from .Models.brand import *
from .Models.model import *
from .Models.colour import *
from .Models.fuel import *
from .Models.variant import *
from .Models.dealbreakup import *

admin.site.register(Brand)
admin.site.register(Model)
admin.site.register(Fuel)
admin.site.register(Variant)
admin.site.register(Colour)
admin.site.register(Dealbreakup)