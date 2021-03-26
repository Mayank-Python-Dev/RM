from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

from master.forms import CustomUserCreationForm, CustomUserChangeForm


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email', 'username',
                    'first_name', 'last_name', 'dealershipname', ]
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('dealershipname', )}),
    )


admin.site.register(CustomUser, CustomUserAdmin)
