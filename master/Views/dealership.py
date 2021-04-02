from django.shortcuts import render, redirect

from ..models import *

from ..forms import *

from django.contrib import messages

from ..Models.brand import *

from login.decorators import *

from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.decorators import login_required



# def createdealership(request):
# 	if request.method =="POST":
# 		form = Dealershipform(request.POST)
# 		if form.is_valid():
# 			form.save()

# 			messages.success(request,f'DEALERSHIP CREATED')
# 			return redirect('dealershipview')
			
# 	form = Dealershipform()
# 	context = {'form' : form}
# 	return render(request,'createdealershipandaccounts/dealership.html',context)