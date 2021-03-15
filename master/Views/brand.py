from django.shortcuts import render, redirect

from ..models import *

from ..forms import *


def brandlist(request):
   if request.method =='POST':
   	form = Brandform(request.POST)
   	if form.is_valid():
   		form.save()	
   		return redirect('brand')

   else:
   	form = Brandform()
   	brands = Brand.objects.all()
   	context = {'brands' : brands,'form':form}
   	return render(request,'brands.html',context)
