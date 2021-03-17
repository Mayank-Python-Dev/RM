from django.shortcuts import render, redirect

from ..forms import *



def pricelist(request):
	
	if request.method == "POST":
		form = Pricelistform(request.POST)
		if form.is_valid():
			form.save()
			
			return redirect('master')

	else:
		form = Pricelistform()
		context = {'form':form}
		return render(request,'master/masterform.html',context)