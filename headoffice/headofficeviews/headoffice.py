from django.shortcuts import render, redirect

from sales.models import Salesbooking

from django.contrib import messages

from django.contrib.messages import constants

from login.decorators import *

from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.decorators import login_required


from master.Models.dealership import *


@login_required(login_url='login')
@allowed_users(allowed_roles=['Ho'])
def Dashboard(request):
    bookings = Salesbooking.objects.all()
    context = {'bookings': bookings}
    return render(request, 'headoffice/headofficedashboard.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['Ho'])
def approve(request, pk):
    bookings = Salesbooking.objects.get(booking_ID=pk)
    if request.method == 'POST':
        bookings.save()

        messages.add_message(request, constants.SUCCESS, f"APPROVED")
        return redirect('headoffice')

    context = {'bookings': bookings}
    return render(request, 'approve headoffice/approvebooking.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['Ho'])
def reject(request, pk):
    bookings = Salesbooking.objects.get(booking_ID=pk)
    if request.method == 'POST':
        bookings.save()
        messages.add_message(request, constants.SUCCESS, f"REJECTED")
        return redirect('headoffice')

    context = {'bookings': bookings}
    return render(request, 'reject headoffice/rejectbooking.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['Ho'])
def bookingdetail(request, pk=None):
    bookings = Salesbooking.objects.filter(booking_ID=pk)
    # detail = bookings.getDict()
    context = {'bookings': bookings}
    return render(request, 'headoffice/headofficebookingdetail.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['Ho'])
def dealership(request):
    Dealerships = Dealership.objects.all()
    context = {'Dealerships': Dealerships}
    return render(request, 'headofficedealership/Dealership.html', context)
