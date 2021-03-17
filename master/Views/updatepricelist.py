from django.shortcuts import render, redirect

from ..forms import *

from ..Models.dealbreakup import *


def UpdatePriceList(request,pk):
	Forms = Dealbreakup.objects.get(id=pk)
	form = Pricelistform(instance = Forms)

	if request.method == "POST":
		form = Pricelistform(request.POST, instance = Forms) 
		if form.is_valid():
			form.save()
			return redirect('master')

	context = {'form':form}
	return render(request,'master/masterform.html',context)