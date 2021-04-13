from django.shortcuts import render, redirect

from ..models import *

from ..forms import *

from django.contrib import messages

from login.decorators import *

from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.decorators import login_required


@login_required(login_url='login')
@allowed_users(allowed_roles=['Master'])
def modellist(request):

    if request.method == "POST":
        form = Modelform(request.POST)
        if form.is_valid():
            form.save()

            messages.success(request, f'MODEL ADDED!')
            form = Modelform()
            context = {'form': form}
            return redirect('model')

        else:
            messages.warning(request, f'MODEL ALREADY EXISTS!')
            form = Modelform()
            return redirect('model')

    else:
        form = Modelform()
        models = Model.objects.all()
        context = {'models': models, 'form': form}
        return render(request, 'master/models.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['Master'])
def updatemodel(request, pk):
    Data = Model.objects.get(id=pk)
    Form = Modelform(instance=Data)

    if request.method == 'POST':
        form = Modelform(request.POST, instance=Data)
        if form.is_valid():
            form.save()

            messages.info(request, f'MODEL UPDATED!')
            return redirect('model')

    context = {'Form': Form}
    return render(request, 'updatemaster/updatemodel.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['Master'])
def deletemodel(request, pk):
    model = Model.objects.get(id=pk)
    if request.method == "POST":
        model.delete()
        messages.warning(request, f'MODEL DELETED!')
        return redirect('model')

    context = {'model': model}
    return render(request, 'deletemaster/deletemodel.html', context)
