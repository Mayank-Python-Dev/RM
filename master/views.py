from django.shortcuts import render

# Create your views here.

from .Models.brand import *
from .Models.model import *
from .Models.colour import *
from .Models.fuel import *
from .Models.variant import *
from .Models.dealbreakup import *



def dashboard(request):
	forms = Dealbreakup.objects.all()
	context = {'forms':forms}
	return render(request, 'master/masterdashboard.html', context)

# AJAX
def load_models(request):
    brand_id = request.GET.get('brand_id')
    models = Model.objects.filter(brand_id=brand_id).all()
    return render(request, 'master/model_dropdown.html', {'models': models})


def logout(request):
	return render(request,'registration/login.html')
 