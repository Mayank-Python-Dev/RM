from django.shortcuts import render, redirect

from ..models import *

from ..forms import *


def modellist(request):
	if request.method == "POST":
		form = Modelform(request.POST)
		if form.is_valid():
			form.save()
			return redirect('model')

	else:
		form = Modelform()
		models = Model.objects.all()
		context = {'models' : models,'form':form}
		return render(request,'models.html',context)

