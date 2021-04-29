from django.http import HttpResponse

from django.shortcuts import render, redirect


def unauthenticated_admin(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('master')
        else:
            return view_func(request, *args, **kwargs)

    return wrapper_func


def allowed_users(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):

            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name

            if group in allowed_roles:
                return view_func(request, *args, **kwargs)

            else:
                return HttpResponse("<p>You are not authorized to view this page</p>")

        return wrapper_func

    return decorator


def admin_only(view_func):
    def wrapper_function(request, *args, **kwargs):
        group = None
        if request.user.groups.exists():
            group = request.user.groups.all()[0].name

        if group == 'HeadOffice':
            return redirect('headoffice')

        if group == 'Sales':
            return redirect('sales')

        if group == 'Account':
            return redirect('actdashboard')

        if group == 'edp':
            return redirect('edpdashboard')

        if group == 'Master':
            return view_func(request, *args, **kwargs)


        else:
            return HttpResponse('Error404')

    return wrapper_function
