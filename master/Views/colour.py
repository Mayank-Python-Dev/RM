from django.shortcuts import render, redirect

from ..models import *

from ..forms import *


def colourlist(request):
	if request.method == "POST":
		form = Colourform(request.POST)
		if form.is_valid():
			form.save()

			return redirect('colour')

	else:
		form = Colourform()
		colours = Colour.objects.all()
		context = {'colours':colours,'form':form}
		return render(request,'colours.html',context)