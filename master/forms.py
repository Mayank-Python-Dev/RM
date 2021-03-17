from django import forms


from .Models.brand import *
from .Models.model import *
from .Models.colour import *
from .Models.fuel import *
from .Models.variant import *
from .Models.dealbreakup import *



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


class Pricelistform(forms.ModelForm):
	class Meta:
		model = Dealbreakup
		fields = "__all__"


	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields['model'].queryset = Model.objects.none()

		if 'brand' in self.data:
			try:
				brand_id = int(self.data.get('brand'))
				self.fields['model'].queryset = Model.objects.filter(brand_id=brand_id).order_by('Name')
			except (ValueError, TypeError):
				pass  # invalid input from the client; ignore and fallback to empty City queryset
		elif self.instance.pk:
			self.fields['model'].queryset = self.instance.brand.model_set.order_by('Name')