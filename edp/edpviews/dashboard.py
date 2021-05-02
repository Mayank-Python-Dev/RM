from django.shortcuts import render

from django.shortcuts import render, redirect

from edp.forms import Edpform

from sales.models import *

from django.contrib import messages

from edp.models import *

from login.decorators import *

from django.contrib.auth.decorators import login_required

from account.models import *

@login_required(login_url='login')
@allowed_users(allowed_roles=['edp'])
def edpdashboard(request):
	Data = Salesbooking.objects.all()
	Dms_status = Uploadfile.objects.all()
	context = {'Data': Data}
	return render(request,'edp/edpdashboard.html', context)



@login_required(login_url='login')
@allowed_users(allowed_roles=['edp'])
def edpform(request,pk):
	Data = Salesbooking.objects.filter(id=pk)
	paymentstatus = TotalPayment.objects.filter(Booking_ID = pk)
	form = Edpform()
	if request.method == "POST":
		# form['ID']=Salesbooking.objects.filter(id=pk)
		# for o in Salesbooking.objects.all():
		# 	t = Uploadfile.create(ID=o)
		# 	t.save()
		form = Edpform(request.POST,request.FILES)
		if form.is_valid():
			instance = form.save(commit=False)
			inv = Salesbooking.objects.get(id=pk)
			instance.ID = inv
			print(instance)
			instance.save()
			messages.success(request,f'DOCUMENTS UPLOADED!')
			return redirect('edpdashboard')
		else:
			messages.warning(request,f'NOT UPLOADED')
			return redirect('edpdashboard')

	form =Edpform()
	context = {'form':form ,'Data': Data,'paymentstatus':paymentstatus }
	return render(request,'edp/create_DMS&Tally.html',context)