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

from django.contrib.auth.models import Group, User

from master.forms import CustomUserCreationForm, CustomUserChangeForm

from users.admin import *


def select_groups(request):
    users = CustomUser.objects.all()
    context = {'users': users}
    return render(request, 'createdealershipandaccounts/groups.html', context)


def update_groups(request, pk):
    Users = CustomUser.objects.get(id=pk)
    form = CustomUserCreationForm(instance=Users)

    if request.method == "POST":
        form = CustomUserCreationForm(request.POST, instance=Users)
        if form.is_valid():
            form.save()

            messages.info(request, f'USER UPDATED!')
            return redirect('groups')

    context = {'form': form}
    return render(request, 'updatemaster/updategroups.html', context)


def delete_groups(request, pk):
    Users = CustomUser.objects.get(id=pk)
    if request.method == "POST":
        Users.delete()
        messages.warning(request, f'USER DELETED!')
        return redirect('groups')

    context = {'Users': Users}
    return render(request, 'deletemaster/deletegroups.html', context)


def register_sales(request):
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']
        if password1 == password2:
            if CustomUser.objects.filter(username=username).exists():
                messages.warning(request, f'USERNAME TAKEN!')
                return redirect('registersales')
            elif CustomUser.objects.filter(email=email).exists():
                messages.warning(request, f'EMAIL TAKEN!')
                return redirect('registersales')
            else:
                form = CustomUserCreationForm(request.POST)
                if form.is_valid():
                    user = form.save()
                    messages.success(request, f'SALES ACCOUNT CREATED!')
                    # username = form.cleaned_data.get('username')
                    group = Group.objects.get(name='Sales')
                    user.groups.add(group)
                    return redirect('registersales')
        else:
            messages.info(request, f'PASSWORD IS NOT MATCHED!')
            return redirect('registersales')

    else:
        form = CustomUserCreationForm()
        return render(request, 'createdealershipandaccounts/createsalesaccount.html', {'form': form})


def register_headoffice(request):
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']
        if password1 == password2:
            if CustomUser.objects.filter(username=username).exists():
                messages.warning(request, f'USERNAME TAKEN!')
                return redirect('registerheadoffice')
            elif CustomUser.objects.filter(email=email).exists():
                messages.warning(request, f'EMAIL TAKEN!')
                return redirect('registerheadoffice')
            else:
                form = CustomUserCreationForm(request.POST)
                if form.is_valid():
                    user = form.save()
                    messages.success(request, f'HEADOFFICE ACCOUNT CREATED!')
                    print(user)
                    username = form.cleaned_data.get('username')
                    group = Group.objects.get(name='Ho')
                    user.groups.add(group)
                    return redirect('registerheadoffice')
        else:
            messages.info(request, f'PASSWORD IS NOT MATCHED!')
            return redirect('registerheadoffice')

    else:
        form = CustomUserCreationForm()
        return render(request, 'createdealershipandaccounts/createheadoffice.html', {'form': form})


def dealership(request):
    if request.method == "POST":
        form = Dealershipform(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'DEALERSHIP CREATED')
            return redirect('dealershipview')

    form = Dealershipform()
    Dealerships = Dealership.objects.all()
    context = {'Dealerships': Dealerships, 'form': form}
    return render(request, 'createdealershipandaccounts/dealershipview.html', context)


def updatedealership(request, pk):
    Dealerships = Dealership.objects.get(id=pk)
    form = Dealershipform(instance=Dealerships)

    if request.method == "POST":
        form = Dealershipform(request.POST, instance=Dealerships)
        if form.is_valid():
            form.save()

            messages.info(request, f'DEALERSHIP UPDATED!')

            return redirect('dealershipview')

    context = {'form': form}
    return render(request, 'updatemaster/updatedealership.html', context)


def deletedealership(request, pk):
    Dealerships = Dealership.objects.get(id=pk)
    if request.method == "POST":
        Dealerships.delete()
        messages.warning(request, f'DEALERSHIP DELETED!')
        return redirect('dealershipview')

    context = {'Dealerships': Dealerships}
    return render(request, 'deletemaster/deletedealership.html', context)


def register_edp(request):
    if request.method == "POST":
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']
        if password1 == password2:
            if CustomUser.objects.filter(username=username).exists():
                messages.warning(request, f'USERNAME TAKEN!')
                return redirect('registeredp')
            elif CustomUser.objects.filter(email=email).exists():
                messages.warning(request, f'EMAIL TAKEN!')
                return redirect('registeredp')
            else:
                form = CustomUserCreationForm(request.POST)
                if form.is_valid():
                    user = form.save()
                    messages.success(request, f'EDP ACCOUNT CREATED!')
                    username = form.cleaned_data.get('username')
                    group = Group.objects.get(name='edp')
                    user.groups.add(group)
                    return redirect('registeredp')
        else:
            messages.info(request, f'PASSWORD IS NOT MATCHED!')
            return redirect('registeredp')

    else:
        form = CustomUserCreationForm()
        return render(request, 'createdealershipandaccounts/createedp.html', {'form': form})


def register_account(request):
    if request.method == "POST":
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']
        if password1 == password2:
            if CustomUser.objects.filter(username=username).exists():
                messages.warning(request, f'USERNAME TAKEN!')
                return redirect('registeraccount')
            elif CustomUser.objects.filter(email=email).exists():
                messages.warning(request, f'EMAIL TAKEN!')
                return redirect('registeraccount')
            else:
                form = CustomUserCreationForm(request.POST)
                if form.is_valid():
                    user = form.save()
                    messages.success(request, f'ACCOUNT CREATED!')
                    username = form.cleaned_data.get('username')
                    group = Group.objects.get(name='account')
                    user.groups.add(group)
                    return redirect('registeraccount')
        else:
            messages.info(request, f'PASSWORD IS NOT MATCHED!')
            return redirect('registeraccount')

    else:
        form = CustomUserCreationForm()
        return render(request, 'createdealershipandaccounts/createaccount.html', {'form': form})
