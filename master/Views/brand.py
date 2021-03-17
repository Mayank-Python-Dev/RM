from django.shortcuts import render, redirect

from ..models import *

from ..forms import *

from django.contrib import messages

from ..Models.brand import *

def brandlist(request):
   if request.method =='POST':
   	form = Brandform(request.POST)
   	if form.is_valid():
         form.save()
         
         messages.success(request,f'BRAND ADDED!')
         form  = Brandform()
         context = {'form': form}
         return redirect('brand')

   else:
   	form = Brandform()
   	brands = Brand.objects.all()
   	context = {'brands' : brands,'form':form}
   	return render(request,'master/brands.html',context)


def updatebrand(request,pk):
   Data = Brand.objects.get(id=pk)
   Form = Brandform(instance = Data)

   if request.method =='POST':
      form = Brandform(request.POST,instance = Data)
      if form.is_valid():
         form.save()

         return redirect('brand')
         


   context = {'Form':Form}
   return render(request,'updatemaster/updatebrand.html',context)


def deletebrand(request,pk):
      brand = Brand.objects.get(id=pk)
      if request.method == "POST":
         brand.delete()
         return redirect('brand')


      context = {'brand' : brand}
      return render(request , 'deletemaster/deletebrand.html' , context)


