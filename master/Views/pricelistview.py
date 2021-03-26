from django.shortcuts import render, redirect

from ..models import *

from ..forms import *


from login.decorators import *

from ..Models.dealbreakup import *

from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.decorators import login_required


@login_required(login_url='login')
@allowed_users(allowed_roles=['Master'])
def Pricelistview(request, pk):
    Forms = Dealbreakup.objects.filter(id=pk)

    context = {'Forms': Forms}
    return render(request, 'master/Pricelistview.html', context)
