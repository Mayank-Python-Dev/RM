from django.shortcuts import render

# Create your views here.


def edppayment(request):
    context = {}
    return render(request, 'edp/edppayment.html', context)
