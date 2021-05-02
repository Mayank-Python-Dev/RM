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
    formset = PaymentFormSet(queryset = CreatePayment.objects.none(),instance = customerID)
    if request.method == "POST":
        formset = PaymentFormSet(request.POST,instance=customerID)

        if formset.is_valid():
            formset.save()
            # formset.Total_Amount = total
            # formset.save(update_fields = ['Total_Amount'])
            # x.save()

                

            return redirect('customer',pk)
    context = {'formset':formset,'customers':customers}
    return render(request,'act/paymentregister.html',context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['Account'])
def customer(request,pk):
    customer = Salesbooking.objects.get(id=pk)
    customers  = CreatePayment.objects.filter(BookingID=pk)
    sum = customers.aggregate(Sum('Amount'))
    total = sum['Amount__sum']
    if total is None:
        total = 0
    #calculation
    onroad = customer.On_Road_Price
    difference = total -  onroad
    pay = TotalPayment.objects.update_or_create(Booking_ID = customer, defaults={'Total_Payment':total,'Difference' : difference})
    payment = TotalPayment.objects.get(Booking_ID = pk)
    customer = Salesbooking.objects.get(id=pk)
    if payment.Total_Payment >= customer.On_Road_Price:
        payment.Payment_Status = "Payment Received"
        payment.save()
        customer.status = "Payment Received"
        customer.save()
        
        
        
    else:
        payment.Payment_Status = "Not Received"
        payment.save()
        customer.status = "Clearance Pending"
        customer.save()
        
        

    customer_payment = TotalPayment.objects.filter(Booking_ID = pk)

        



    # pay.save()
    # pid = CreatePayment.objects.get(BookingID=pk)
    # pay = TotalPayment.objects.all()
    # pay.Payment_ID = pid
    # pay.Total_Payment = total
    # pay.save()
    # or p.save(save_fields=['question'])
    
    # val = CreatePayment.objects.filter(BookingID=customers).update(Total_Amount=F('Total_Amount') + 1)
    # # val.Total_Amount = x
    # # val.save(update_fields = ['Total_Amount'])
    # print(val)
    # val.save()

    context = {'customer':customer,'customers':customers,'customer_payment':customer_payment}
    return render(request,'act/customer.html',context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['Account'])
def updatepayment(request,pk):
    customers  = CreatePayment.objects.get(id=pk)
    cid = customers.BookingID

    # PaymentFormSet = inlineformset_factory(Salesbooking,CreatePayment,fields = ('BookingID','Payment_Method','Amount','Date'))
    form = PaymentForm(instance = customers)
    if request.method == "POST":
        form = PaymentForm(request.POST,instance=customers)
        if form.is_valid():
            form.save()
            sid = Salesbooking.objects.get(booking_ID = cid)
            revid = sid.id
            return redirect('customer',revid)
    context = {'form':form}
    return render(request,'act/updatepayment.html',context)



@login_required(login_url='login')
@allowed_users(allowed_roles=['Account'])
def deletepayment(request,pk):
    customers  = CreatePayment.objects.get(id=pk)
    cid = customers.BookingID
    if request.method == "POST":
        customers.delete()
        sid = Salesbooking.objects.get(booking_ID = cid)
        revid = sid.id
        return redirect('customer',revid)

    context = {}
    return render(request,'act/deletepayment.html',context)

