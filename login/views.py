from django.shortcuts import render , redirect



from django.http import HttpResponse, JsonResponse
from .models import *
from django.contrib import messages

from .decorators import *

from django.contrib.auth import authenticate , login , logout 

from django.contrib.auth.decorators import login_required


@unauthenticated_admin
def loginPage(request):

    if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request,username=username,password=password)

            if user is not None:
                login(request,user)
                return redirect('master')
            else:
                messages.info(request,'Username OR Password is Incorrect')


    return render(request,'login.html')



def logoutPage(request):
    logout(request)
    return redirect('login')