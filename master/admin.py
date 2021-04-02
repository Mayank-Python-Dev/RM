from django.contrib import admin

# Register your models here.
from .Models.brand import *
from .Models.model import *
from .Models.colour import *
from .Models.fuel import *
from .Models.variant import *
from .Models.dealbreakup import *
from .Models.dealership import *

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

# from .models import CustomUser

admin.site.register(Brand)
admin.site.register(Model)
admin.site.register(Fuel)
admin.site.register(Variant)
admin.site.register(Colour)
admin.site.register(Dealbreakup)
admin.site.register(Dealership)

# class CustomerUserAdmin(UserAdmin):
# 	add_form = UserCreationForm
# 	form = UserChangeForm
# 	model = CustomUser
# 	list_displays = ['pk', 'email', 'username', 'first_name', 'last_name','Dealership']

# 	add_fieldsets = UserAdmin.add_fieldsets + (
#     (None, {'fields': ('Dealership',)}),
# )
# 	fieldsets = UserAdmin.fieldsets


# admin.site.register(CustomUser,CustomerUserAdmin)
