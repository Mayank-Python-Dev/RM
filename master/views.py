from django.shortcuts import render, redirect

# Create your views here.
from django.contrib import messages
from .Models.brand import *
from .Models.model import *
from .Models.colour import *
from .Models.fuel import *
from .Models.variant import *
from .Models.dealbreakup import *

from login.decorators import *

from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.decorators import login_required


@login_required(login_url='login')
@admin_only
def dashboard(request):
    forms = Dealbreakup.objects.all()
    context = {'forms': forms}
    return render(request, 'master/masterdashboard.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['Master'])
def deletedeal(request, pk):
    Deal = Dealbreakup.objects.get(id=pk)
    if request.method == "POST":
        Deal.delete()
        messages.warning(request, f'PRICELIST DELETED!')
        return redirect('master')

    context = {'Deal': Deal}
    return render(request, 'deletemaster/deletedeal.html', context)


# AJAX
@login_required(login_url='login')
@allowed_users(allowed_roles=['Master'])
def load_models(request):
    brand_id = request.GET.get('brand_id')
    models = Model.objects.filter(brand_id=brand_id).all()
    return render(request, 'ajax/model_dropdown.html', {'models': models})

# AJAX


@login_required(login_url='login')
@allowed_users(allowed_roles=['Master'])
def load_fuels(request):
    model_id = request.GET.get('model_id')
    fuels = Fuel.objects.filter(model_id=model_id).all()
    return render(request, 'ajax/fuel_dropdown.html', {'fuels': fuels})

# AJAX


@login_required(login_url='login')
@allowed_users(allowed_roles=['Master'])
def load_variants(request):
    fuel_id = request.GET.get('fuel_id')
    variants = Variant.objects.filter(fuel_id=fuel_id).all()
    return render(request, 'ajax/variant_dropdown.html', {'variants': variants})


@login_required(login_url='login')
@allowed_users(allowed_roles=['Master'])
def load_colours(request):
    variant_id = request.GET.get('variant_id')
    colours = Colour.objects.filter(variant_id=variant_id).all()
    return render(request, 'ajax/colour_dropdown.html', {'colours': colours})


@login_required(login_url='login')
@allowed_users(allowed_roles=['Master'])
def logout(request):
    return render(request, 'registration/login.html')
