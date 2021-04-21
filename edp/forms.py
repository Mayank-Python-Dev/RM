from django import forms

from .models import *

from django.forms import ModelForm
class Edpform(ModelForm):
	class Meta:
		model = Uploadfile
		fields = ['DMS','Tally']