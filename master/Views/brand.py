from django.shortcuts import render, redirect

from ..models import *

from ..forms import *

from django.contrib import messages

from ..Models.brand import *

from login.decorators import *

from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.decorators import login_required


@login_required(login_url='login')
@allowed_users(allowed_roles=['Master'])
def brandlist(request):
    if request.method == 'POST':
        form = Brandform(request.POST)
        if form.is_valid():
            form.save()

            messages.success(request, f'BRAND ADDED!')
            form = Brandform()
            context = {'form': form}
            return redirect('brand')

        else:
            messages.warning(request, f'BRAND ALREADY EXISTS')
            form = Brandform()
            context = {'form': form}
            return redirect('brand')
    else:
        form = Brandform()
        brands = Brand.objects.all()
        context = {'brands': brands, 'form': form}
        return render(request, 'master/brands.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['Master'])
def updatebrand(request, pk):
    Data = Brand.objects.get(id=pk)
    Form = Brandform(instance=Data)

    if request.method == 'POST':
        form = Brandform(request.POST, instance=Data)
        if form.is_valid():
            form.save()

            messages.info(request, f'BRAND UPDATED!')
            return redirect('brand')

    context = {'form': form}
    return render(request, 'updatemaster/updatebrand.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['Master'])
def deletebrand(request, pk):
    brand = Brand.objects.get(id=pk)
    if request.method == "POST":
        brand.delete()

        messages.warning(request, f'BRAND DELETED!')
        return redirect('brand')

    context = {'brand': brand}
    return render(request, 'deletemaster/deletebrand.html', context)
