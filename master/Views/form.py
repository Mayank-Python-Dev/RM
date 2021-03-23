from django.shortcuts import render, redirect

from ..forms import *

from login.decorators import *

from django.contrib import messages

from django.contrib.auth import authenticate , login , logout 

from django.contrib.auth.decorators import login_required


@login_required(login_url = 'login')
@allowed_users(allowed_roles=['Master'])
def pricelist(request):
	
	if request.method == "POST":
		form = Pricelistform(request.POST)
		if form.is_valid():
			form.save()
			
			messages.success(request,f'PRICE LIST ADDED!')
			form  = Pricelistform()
			context = {'form': form}
			return redirect('master')

	else:
		form = Pricelistform()
		context = {'form':form}
		return render(request,'master/masterform.html',context)