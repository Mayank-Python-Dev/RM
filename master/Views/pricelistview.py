from django.shortcuts import render, redirect

from ..models import *

from ..forms import *

from ..Models.dealbreakup import *

def Pricelistview(request,pk):
	Forms = Dealbreakup.objects.filter(id=pk)

	context = {'Forms': Forms}
	return render(request,'master/Pricelistview.html',context)
