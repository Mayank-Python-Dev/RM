from django.shortcuts import render, redirect

from sales.models import Salesbooking

from django.contrib import messages

from django.contrib.messages import constants

from login.decorators import *

from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.decorators import login_required

from django.http import HttpResponse

from master.Models.dealership import *

from sales.forms import *

from django.http import JsonResponse

from django.core import serializers


@login_required(login_url='login')
@allowed_users(allowed_roles=['HeadOffice'])
def Dashboard(request):
    bookings = Salesbooking.objects.all()
    context = {'bookings': bookings}
    return render(request, 'headoffice/headofficedashboard.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['HeadOffice'])
def approve(request, pk):
    bookings = Salesbooking.objects.get(booking_ID=pk)
    if request.method == 'POST':
        bookings.status = 'Approved'
        bookings.save()

        return redirect('headoffice')

    context = {'bookings': bookings}
    return render(request, 'approve headoffice/approvebooking.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['HeadOffice'])
def reject(request, pk):
    bookings = Salesbooking.objects.get(booking_ID=pk)
    if request.method == 'POST':
        bookings.status = 'Rejected'
        bookings.save()

        return redirect('headoffice')

    context = {'bookings': bookings}
    return render(request, 'reject headoffice/rejectbooking.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['HeadOffice'])
def bookingdetail(request, pk):
    Data = Salesbooking.objects.get(id=pk)
    Form = Bookingform(instance=Data)
    if request.method == 'POST':
        Form = Bookingform(request.POST, instance=Data)
        if Form.is_valid():
            Form.save()

            messages.success(request, f'MODIFICATION SENT TO SALES!')
            return redirect('headoffice')

    context = {'Form': Form}
    return render(request, 'headoffice/headofficebookingdetail.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['HeadOffice'])
def dealership(request):
    Dealerships = Dealership.objects.all()
    context = {'Dealerships': Dealerships}
    return render(request, 'headofficedealership/Dealership.html', context)


# def modification(request, pk):
#     bookings = Salesbooking.objects.filter(booking_ID=pk)
#     if request.method == "POST":
#         form = ModificationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponse('data has been sent')

#     else:
#         form = ModificationForm()
#         context = {'form': form}
#         return render(request, 'modify headoffice/modifyheadoffice.html', context)

    # qs = Salesbooking.objects.all()
    # qs_json = serializers.serialize('json', qs)
    # return HttpResponse(qs_json, content_type='application/json')
