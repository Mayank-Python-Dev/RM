from django.shortcuts import render

# Create your views here.
from .models import *

def dashboard(request):
    context = {}
    return render(request, 'masterdashboard.html', context)
