from django.shortcuts import render

# Create your views here.


def actdashboard(request):
    context = {}
    return render(request, 'act/actdashboard.html', context)
