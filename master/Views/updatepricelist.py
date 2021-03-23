from django.shortcuts import render, redirect

from ..forms import *

from ..Models.dealbreakup import *

from login.decorators import *

from django.contrib import messages

from django.contrib.auth import authenticate , login , logout 

from django.contrib.auth.decorators import login_required



@login_required(login_url = 'login')
@allowed_users(allowed_roles=['Master'])
def UpdatePriceList(request,pk):
	Forms = Dealbreakup.objects.get(id=pk)
	form = Pricelistform(instance = Forms)

	if request.method == "POST":
		form = Pricelistform(request.POST, instance = Forms) 
		if form.is_valid():
			form.save()

			messages.success(request,f'PRICE LIST UPDATED!')
			form  = Pricelistform()
			context = {'form': form}
			return redirect('master')

	context = {'form':form}
	return render(request,'master/masterform.html',context)