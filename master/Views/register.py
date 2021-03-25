from django.shortcuts import render, redirect

from ..models import *

from ..forms import *

from django.contrib import messages

from ..Models.brand import *

from login.decorators import *

from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.decorators import login_required

from django.contrib.auth.forms import UserCreationForm

from django.http import HttpResponse

from users.models import CustomUser

from django.contrib.auth.models import Group


def select_groups(request):
    return render(request, 'createdealershipandaccounts/groups.html')


def register_sales(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, f'ACCOUNT CREATED!')
            username = form.cleaned_data.get('username')
            group = Group.objects.get(name='Sales')
            user.groups.add(group)
            return redirect('registersales')
        else:
            messages.warning(request, f'USERNAME IS ALREADY EXISTS!')
            return redirect('registersales')

    else:
        form = CustomUserCreationForm()
        return render(request, 'createdealershipandaccounts/createsalesaccount.html', {'form': form})


def register_headoffice(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            print(user)
            username = form.cleaned_data.get('username')
            group = Group.objects.get(name='Ho')
            user.groups.add(group)
            return redirect('groups')

    else:
        form = CustomUserCreationForm()
        return render(request, 'createdealershipandaccounts/createheadoffice.html', {'form': form})


# def register_sales(request):
#     if request.method == 'POST':
#         form = CreateUserForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             print(user)
#             username = form.cleaned_data.get('username')
#             group = Group.objects.get(name = 'Sales')
#             user.groups.add(group)
#             return redirect('register')

#     else:
#         form = CreateUserForm()
#         return render(request, 'createdealershipandaccounts/createsalesaccount.html', {'form':form})


# def register_sales(request):
#     if request.method == 'POST':
#         form = CreateUserForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             print(user)
#             username = form.cleaned_data.get('username')
#             group = Group.objects.get(name = 'Sales')
#             user.groups.add(group)
#             return redirect('register')

#     else:
#         form = CreateUserForm()
#         return render(request, 'createdealershipandaccounts/createsalesaccount.html', {'form':form})


def dealership(request):
    Dealerships = Dealership.objects.all()
    context = {'Dealerships': Dealerships}
    return render(request, 'createdealershipandaccounts/dealershipview.html', context)
