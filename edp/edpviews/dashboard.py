from django.shortcuts import render

from django.shortcuts import render, redirect

from edp.forms import Edpform

from sales.models import *

from django.contrib import messages

from edp.models import *

def edpdashboard(request):
	Data = Salesbooking.objects.all()
	print(Data)
	context = {'Data': Data}
	return render(request,'edp/edpdashboard.html', context)

def edpform(request,pk):
	Data = Salesbooking.objects.filter(id=pk)
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
			# obj = form.save(commit=False) # Return an object without saving to the DB
			# obj.ID = Salesbooking.objects.get(id=pk)
			# print(obj.ID) # Add an author field which will contain current user's id
			# obj.save() # Save the final "real form" to the DB
			# form.save()

			
			messages.success(request,f'DOCUMENTS UPLOADED!')
			return redirect('edpdashboard')
		else:
			messages.warning(request,f'NOT UPLOADED')
			return redirect('edpdashboard')

	form =Edpform()
	context = {'form':form ,'Data': Data }
	return render(request,'edp/create_DMS&Tally.html',context)