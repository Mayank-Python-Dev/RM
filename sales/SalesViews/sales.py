from django.shortcuts import render, redirect

from django.http import JsonResponse

from django.core import serializers

from sales.forms import *

from login.decorators import *

from master.Models.dealbreakup import Dealbreakup

from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.decorators import login_required

from django.contrib import messages

from django.contrib.auth.models import User


@login_required(login_url='login')
@allowed_users(allowed_roles=['Sales'])
def Booking(request):

    if request.method == "POST":
        Form = Bookingform(request.POST, request.FILES)
        if Form.is_valid():
            Form.save()
            messages.success(request, f'BOOKING CREATED!')
            Form = Bookingform()
            context = {'Form': Form}
            return redirect('sales')
    else:

        Form = Bookingform()
        bookings = Salesbooking.objects.all()

        context = {'Form': Form, 'bookings': bookings}
        return render(request, 'sales/booking.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['Sales'])
def Dashboard(request):
    bookings = Salesbooking.objects.all()
    context = {'bookings': bookings}
    return render(request, 'sales/salesdashboard.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['Sales'])
def Detail(request):
    brand = request.GET['brand']
    model = request.GET['model']
    #fuel = request.GET['fuel']
    variant = request.GET['variant']
    color = request.GET['color']
    dbres = Dealbreakup.objects.select_related('brand', 'model', 'variant', 'colour').filter(
        brand=brand, model=model, variant=variant, colour=color)

    res = serializers.serialize("json", dbres)
    data = {"data": res}
    return JsonResponse(data)


@login_required(login_url='login')
@allowed_users(allowed_roles=['Sales'])
def DropdownData(request):
    tp = request.GET['type']
    val = request.GET['val']
    #fuel = request.GET['fuel']
    dbres = None
    if tp == "id_Brand":
        dbres = Model.objects.filter(brand=val).all()

    elif tp == "id_Model":
        dbres = Variant.objects.select_related('model').filter(model=val).all()

    elif tp == "id_Variant":
        dbres = Colour.objects.filter(variant=val).all()

    if not dbres:
        res = serializers.serialize("json", dbres)
        data = {"data": res}
        return JsonResponse(data)

    return JsonResponse({"data": ""})

    # dbres = Dealbreakup.objects.select_related('brand','model','variant','colour').filter(tp=val)

    # res = serializers.serialize("json", dbres)
    # data = {"data": res}
    # return JsonResponse(data)


@login_required(login_url='login')
@allowed_users(allowed_roles=['Sales'])
def updatebooking(request, pk):
    bookings = Salesbooking.objects.get(id=pk)
    form = Bookingform(instance=bookings)
    if request.method == "POST":
        form = Bookingform(request.POST, request.FILES, instance=bookings)
        if form.is_valid():
            x = form.cleaned_data['booking_receipt']
            print(x)
            form.save()
            messages.info(request, f'BOOKING UPDATED!')
            return redirect('sales')

    context = {'form': form}
    return render(request, 'updatesales/updatebooking.html', context)


def deletebooking(request, pk):
    bookings = Salesbooking.objects.get(id=pk)
    if request.method == "POST":
        bookings.delete()
        messages.warning(request, f'BOOKING DELETED!')
        return redirect('sales')

    context = {'bookings': bookings}
    return render(request, 'deletesales/deletebooking.html', context)
