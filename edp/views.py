from django.shortcuts import render

# Create your views here.


def edpdashboard(request):
    context = {}
    return render(request, 'edp/edpdashboard.html', context)
