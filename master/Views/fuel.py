from django.shortcuts import render , redirect

from ..models import *
from ..forms import *

def fuellist(request):
	if request.method == "POST":
		form = Fuelform(request.POST)
		if form.is_valid():
			form.save()
			return redirect('fuel')

	else:
		form = Fuelform()
		fuels = Fuel.objects.all()
		context = {'fuels' : fuels,'form':form}
		return render(request,'fuels.html',context)