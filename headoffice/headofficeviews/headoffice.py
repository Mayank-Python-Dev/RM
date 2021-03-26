from django.shortcuts import render, redirect

from sales.models import Salesbooking


def Dashboard(request):
    bookings = Salesbooking.objects.all()
    context = {'bookings': bookings}
    return render(request, 'headoffice/headofficedashboard.html', context)


def approve(request, pk):
    bookings = Salesbooking.objects.get(booking_ID=pk)
    context = {'bookings': bookings}
    return render(request, 'approve headoffice/approvebooking.html', context)


def reject(request, pk):
    bookings = Salesbooking.objects.get(booking_ID=pk)
    context = {'bookings': bookings}
    return render(request, 'reject headoffice/rejectbooking.html', context)


def bookingdetail(request, pk=None):
    bookings = Salesbooking.objects.get(booking_ID=pk)
    detail = bookings.getDict()

    return render(request, 'headoffice/headofficebookingdetail.html', {'detail': detail})


def dealership(request):
    context = {}
    return render(request, 'headofficedealership/Dealership.html', context)
