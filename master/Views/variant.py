from django.shortcuts import render, redirect

from ..models import *

from ..forms import *

from login.decorators import *

from ..Models.variant import *

from django.contrib import messages

from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.decorators import login_required

from master.Models.variant import *


@login_required(login_url='login')
@allowed_users(allowed_roles=['Master'])
def variantlist(request):
    if request.method == "POST":
        form = Variantform(request.POST)
        if form.is_valid():
            name = request.POST.get('Name')
            brandname = request.POST.get('brand')
            modelname = request.POST.get('model')
            fuelname = request.POST.get('fuel')
            if Variant.objects.filter(Name=name, brand=brandname, model=modelname, fuel=fuelname).exists():
                messages.warning(
                    request, f'ALREADY EXISTS!')
                return redirect('variant')
            else:
                form.save()
                messages.success(request, f'VARIANT ADDED!')
                return redirect('variant')

        else:
            messages.warning(request, f'VARIANT ALREADY EXISTS')
            form = Variantform()
            return redirect('variant')

    else:
        form = Variantform()
        variants = Variant.objects.all()
        context = {'variants': variants, 'form': form}
        return render(request, 'master/variants.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['Master'])
def updatevariant(request, pk):
    Data = Variant.objects.get(id=pk)
    Form = Variantform(instance=Data)

    if request.method == 'POST':
        form = Variantform(request.POST, instance=Data)
        if form.is_valid():
            form.save()

            messages.info(request, f'VARIANT UPDATED!')
            return redirect('variant')

    context = {'Form': Form}
    return render(request, 'updatemaster/updatevariant.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['Master'])
def deletevariant(request, pk):
    variant = Variant.objects.get(id=pk)
    if request.method == "POST":
        variant.delete()

        messages.warning(request, f'VARIANT DELETED!')
        return redirect('variant')
    context = {'variant': variant}

    return render(request, 'deletemaster/deletevariant.html', context)
