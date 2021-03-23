from django.shortcuts import render, redirect

from ..models import *

from ..forms import *

from django.contrib import messages

from login.decorators import *

from django.contrib.auth import authenticate , login , logout 

from django.contrib.auth.decorators import login_required

@login_required(login_url = 'login')
@allowed_users(allowed_roles=['Master'])
def colourlist(request):
	if request.method == "POST":
		form = Colourform(request.POST)
		if form.is_valid():
			form.save()

			messages.success(request,f'COLOUR ADDED!')
			form  = Colourform()
			context = {'form': form}
			return redirect('colour')
		else:
			messages.warning(request,f'COLOUR ALREADY EXISTS')
			form = Colourform()
			return redirect('colour')

	else:
		form = Colourform()
		colours = Colour.objects.all()
		context = {'colours':colours,'form':form}
		return render(request,'master/colours.html',context)

@login_required(login_url = 'login')
@allowed_users(allowed_roles=['Master'])
def updatecolour(request,pk):
   Data = Colour.objects.get(id=pk)
   Form = Colourform(instance = Data)


   if request.method =='POST':
      form = Colourform(request.POST,instance = Data)
      if form.is_valid():
         form.save()

         return redirect('colour')
         


   context = {'Form':Form}
   return render(request,'updatemaster/updatecolour.html',context)

@login_required(login_url = 'login')
@allowed_users(allowed_roles=['Master'])
def deletecolour(request,pk):
	colour = Colour.objects.get(id=pk)
	if request.method == "POST":
		colour.delete()
		return redirect('colour')

	context = {'colour':colour}
	return render(request,'deletemaster/deletecolour.html',context)