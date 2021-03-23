from django import forms


from .Models.brand import *

from .Models.model import *

from .Models.colour import *

from .Models.fuel import *

from .Models.variant import *

from .Models.dealbreakup import *

from .Models.dealership import *

from django.contrib.auth.models import User, Group

from django.contrib.auth.forms import UserCreationForm

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


class Dealershipform(forms.ModelForm):
	
	class Meta:
		model = Dealership
		fields = ['Name','address','state','city','pincode']


class CreateUserForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter Username'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Email'}))
    first_name = forms.CharField(label='Firstname', widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Firstname'}))
    last_name = forms.CharField(label='Lastname', widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Lastname'}))
    # groups = forms.ModelChoiceField(label='Role', queryset=Group.objects.all(), widget=forms.Select(attrs={'class':'form-control'}))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Password'}))
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Confirm Password'}))

    class Meta():
        model = User
        fields = ('username','email', 'first_name', 'last_name', 'password1', 'password2')



    # def save(self, commit=True):
    # 	user = super().save(commit=False)
    # 	user.username = self.cleaned_data['username']
    # 	user.email = self.cleaned_data['email']
    # 	user.first_name = self.cleaned_data['first_name']
    # 	user.last_name = self.cleaned_data['last_name']
    # 	user.groups = self.cleaned_data['groups']
    # 	user.password1 = self.cleaned_data['password1']
    # 	user.password2 = self.cleaned_data['password2']

    # 	if commit:
    # 		user.save()
    # 		return user
