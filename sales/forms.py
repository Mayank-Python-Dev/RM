from django import forms

from .models import *

from django.forms import ClearableFileInput


class Bookingform(forms.ModelForm):
    class Meta:
        model = Salesbooking
        fields = "__all__"
