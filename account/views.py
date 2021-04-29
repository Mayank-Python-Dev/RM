from django.shortcuts import render , redirect

# Create your views here.
from .forms import *

from .models import *

from django.http import JsonResponse

from django.forms import inlineformset_factory

from sales.models import *
from django.db.models import Sum

from login.decorators import *

from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
@allowed_users(allowed_roles=['Account'])
def actdashboard(request):
    Data = Salesbooking.objects.all()
    context = {'Data':Data}
    return render(request, 'act/actdashboard.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['Account'])
def createpayment(request,pk):
    PaymentFormSet = inlineformset_factory(Salesbooking,CreatePayment,fields = ('BookingID','Payment_Method','Amount','Date') ,extra = 5)
    customerID = Salesbooking.objects.get(id=pk)
    customers  = CreatePayment.objects.filter(BookingID=pk)
    cust = CreatePayment.objects.filter(id=pk)
    formset = PaymentFormSet(queryset = CreatePayment.objects.none(),instance = customerID)
    if request.method == "POST":
        formset = PaymentFormSet(request.POST,instance=customerID)
        if formset.is_valid():
            formset.save()
                

            return redirect('actdashboard')
    context = {'formset':formset,'customers':customers}
    return render(request,'act/paymentregister.html',context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['Account'])
def customer(request,pk):
    customer = Salesbooking.objects.get(id=pk)
    customers  = CreatePayment.objects.filter(BookingID=pk)
    sum = customers.aggregate(Sum('Amount'))
    total = sum['Amount__sum']
    customers.Total_Amount = total
    x = customers.Total_Amount
    print(x)  
    
    
    context = {'customer':customer,'customers':customers}
    return render(request,'act/customer.html',context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['Account'])
def updatepayment(request,pk):
    customers  = CreatePayment.objects.get(id=pk)
    # PaymentFormSet = inlineformset_factory(Salesbooking,CreatePayment,fields = ('BookingID','Payment_Method','Amount','Date'))
    form = PaymentForm(instance = customers)
    if request.method == "POST":
        form = PaymentForm(request.POST,instance=customers)
        if form.is_valid():
            form.save()
            return redirect('actdashboard')
    context = {'form':form}
    return render(request,'act/updatepayment.html',context)



@login_required(login_url='login')
@allowed_users(allowed_roles=['Account'])
def deletepayment(request,pk):
    customers  = CreatePayment.objects.get(id=pk)
    if request.method == "POST":
        customers.delete() 
        return redirect('actdashboard')

    context = {}
    return render(request,'act/deletepayment.html',context)

