from django.shortcuts import render ,redirect

from ..models import *

from ..forms import *


def variantlist(request):
	if request.method == "POST":
		form = Variantform(request.POST)
		if form.is_valid():
			form.save()
			return redirect('variant')

	else:
		form = Variantform()
		variants = Variant.objects.all()
		context = {'variants' : variants,'form':form}
		return render(request,'variants.html',context)