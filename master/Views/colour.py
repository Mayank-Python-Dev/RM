from django.shortcuts import render, redirect

from ..models import *

from ..forms import *


def colourlist(request):
	if request.method == "POST":
		form = Colourform(request.POST)
		if form.is_valid():
			form.save()

			messages.success(request,f'COLOUR ADDED!')
			form  = Colourform()
			context = {'form': form}
			return redirect('colour')

	else:
		form = Colourform()
		colours = Colour.objects.all()
		context = {'colours':colours,'form':form}
		return render(request,'master/colours.html',context)


def updatecolour(request,pk):
   Data = Colour.objects.get(id=pk)
   Form = Colourform(instance = Data)


   if request.method =='POST':
      form = Colourform(request.POST,instance = Data)
      if form.is_valid():
         form.save()

         return redirect('colour')
         


   context = {'Form':Form}
   return render(request,'updatemaster/updatecolour.html',context)


def deletecolour(request,pk):
	colour = Colour.objects.get(id=pk)
	if request.method == "POST":
		colour.delete()
		return redirect('colour')

	context = {'colour':colour}
	return render(request,'deletemaster/deletecolour.html',context)