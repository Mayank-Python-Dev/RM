from django.shortcuts import render, redirect

from ..models import *

from ..forms import *


def modellist(request):
	if request.method == "POST":
		form = Modelform(request.POST)
		if form.is_valid():
			form.save()

			messages.success(request,f'MODEL ADDED!')
			form  = Modelform()
			context = {'form': form}
			return redirect('model')

	else:
		form = Modelform()
		models = Model.objects.all()
		context = {'models' : models,'form':form}
		return render(request,'master/models.html',context)



def updatemodel(request,pk):
   Data = Model.objects.get(id=pk)
   Form = Modelform(instance = Data)


   if request.method =='POST':
      form = Modelform(request.POST,instance = Data)
      if form.is_valid():
         form.save()

         return redirect('model')
         


   context = {'Form':Form}
   return render(request,'updatemaster/updatemodel.html',context)



def deletemodel(request,pk):
      model = Model.objects.get(id=pk)
      if request.method == "POST":
         model.delete()
         return redirect('model')


      context = {'model' : model}
      return render(request , 'deletemaster/deletemodel.html' , context)