from django import forms


from .models import *



class Brandform(forms.ModelForm):
	class Meta:
		model = Brand
		fields = "__all__"



class Modelform(forms.ModelForm):
	class Meta:
		model = Model
		fields = "__all__"


class Variantform(forms.ModelForm):
	class Meta:
		model = Variant
		fields = "__all__"


class Fuelform(forms.ModelForm):
	class Meta:
		model = Fuel
		fields = "__all__"

class Colourform(forms.ModelForm):
	class Meta:
		model = Colour
		fields = "__all__"