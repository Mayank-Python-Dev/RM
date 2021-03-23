from django.shortcuts import render , redirect

from ..models import *

from ..forms import *


from login.decorators import *

from django.contrib import messages

from django.contrib.auth import authenticate , login , logout 

from django.contrib.auth.decorators import login_required


@login_required(login_url = 'login')
@allowed_users(allowed_roles=['Master'])
def fuellist(request):
	if request.method == "POST":
		form = Fuelform(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request,f'FUEL TYPE ADDED!')
			form  = Fuelform()
			context = {'form': form}
			return redirect('fuel')
		else:
			messages.warning(request,f'FUEL TYPE ALREADY EXISTS')
			form = Fuelform()
			return redirect('fuel')

	else:
		form = Fuelform()
		fuels = Fuel.objects.all()
		context = {'fuels' : fuels,'form':form}
		return render(request,'master/fuels.html',context)


@login_required(login_url = 'login')
@allowed_users(allowed_roles=['Master'])
def updatefuel(request,pk):
   Data = Fuel.objects.get(id=pk)
   Form = Fuelform(instance = Data)


   if request.method =='POST':
      form = Fuelform(request.POST,instance = Data)
      if form.is_valid():
         form.save()

         return redirect('fuel')
         

   context = {'Form':Form}
   return render(request,'updatemaster/updatefuel.html',context)


@login_required(login_url = 'login')
@allowed_users(allowed_roles=['Master'])
def deletefuel(request,pk):
	fuel = Fuel.objects.get(id=pk)
	if request.method == "POST":
		fuel.delete()
		return redirect('fuel')

	context = {'fuel' : fuel}
	return render(request,'deletemaster/deletefuel.html',context)