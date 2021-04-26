from django.shortcuts import render

# Create your views here.
from .forms import *

from .models import *

from django.http import JsonResponse
# from django.views.decorators.csrf import csrf_exempt

from sales.models import *

def actdashboard(request):
    Data = Salesbooking.objects.all()
    context = {'Data':Data}
    return render(request, 'act/actdashboard.html', context)


def paymentbreakup(request,pk):
    key = Salesbooking.objects.filter(id=pk)
    form = PaymentRegistration()
    Data = PaymentBreakUP.objects.all()
    context = {'form': form, 'Data': Data}
    return render(request, 'act/paymentregister.html', context)


# @csrf_exempt
def savedata(request):
    if request.method == "POST":
        form = PaymentRegistration(request.POST)
        if form.is_valid():
            sid = request.POST['payid']
            ID = form.cleaned_data['ID']
            Payment_Method = request.POST['Payment_Method']
            payment = request.POST['payment']
            print(sid,ID)
            if(sid == ''):
                data = PaymentBreakUP(
                ID=ID, Payment_Method=Payment_Method, payment=payment)
            else:
                data = PaymentBreakUP(id=sid,
                ID=ID, Payment_Method=Payment_Method, payment=payment)

            data.save()
            value = PaymentBreakUP.objects.values()
            
            valuelist = list(value)

            return JsonResponse({'status': 'Save', 'valuelist': valuelist})
        else:
            return JsonResponse({'status': 0})


def deletedata(request):
    if request.method == "POST":
        id = request.POST.get('sid')
        # print(id)
        pi = PaymentBreakUP.objects.get(pk = id)
        pi.delete()
        return JsonResponse({'status':1})
    else:
        return JsonResponse({'status':0})


def editdata(request):
    if request.method == "POST":
        id = request.POST.get('sid')
        print(id)
        update = PaymentBreakUP.objects.get(pk=id)
        update_data = {"id" : update.id, "Payment_Method" : update.Payment_Method,"payment" : update.payment}
        return JsonResponse(update_data)
