from django import forms

from .models import *

from master.Models.model import *

from master.Models.brand import *

from django.forms import ClearableFileInput


class Bookingform(forms.ModelForm):
    class Meta:
        model = Salesbooking
        fields = "__all__"


class BookingUpdateform(forms.ModelForm):
    class Meta:
        model = Salesbooking
        fields = ['Modification']
