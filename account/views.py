from django.shortcuts import render , redirect

# Create your views here.
from .forms import *

from .models import *

from django.http import JsonResponse

from django.forms import inlineformset_factory

from sales.models import *

def actdashboard(request):
    Data = Salesbooking.objects.all()
    context = {'Data':Data}
    return render(request, 'act/actdashboard.html', context)


def createpayment(request,pk):
    PaymentFormSet = inlineformset_factory(Salesbooking,CreatePayment,fields = ('BookingID','Payment_Method','Amount'))
    customerID = Salesbooking.objects.get(booking_ID=pk)

    formset = PaymentFormSet(queryset = CreatePayment.objects.none(),instance = customerID)
    if request.method == "POST":
        formset = PaymentFormSet(request.POST,instance=customerID)
        if formset.is_valid():
            formset.save()
            return redirect('actdashboard')

    context = {'form':formset}
    return render(request,'act/paymentregister.html',context)




