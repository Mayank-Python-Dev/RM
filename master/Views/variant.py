from django.shortcuts import render ,redirect

from ..models import *

from ..forms import *

from ..Models.variant import *

def variantlist(request):
	if request.method == "POST":
		form = Variantform(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request,f'VARIANT ADDED!')
			form  = Variantform()
			context = {'form': form}
			return redirect('variant')

	else:
		form = Variantform()
		variants = Variant.objects.all()
		context = {'variants' : variants,'form':form}
		return render(request,'master/variants.html',context)


def updatevariant(request,pk):
   Data = Variant.objects.get(id=pk)
   Form = Variantform(instance = Data)


   if request.method =='POST':
      form = Variantform(request.POST,instance = Data)
      if form.is_valid():
         form.save()

         return redirect('variant')
         


   context = {'Form':Form}
   return render(request,'updatemaster/updatevariant.html',context)


def deletevariant(request,pk):
	variant = Variant.objects.get(id=pk)
	if request.method == "POST":
		variant.delete()

		return redirect('variant')
	context = {'variant':variant}

	return render(request, 'deletemaster/deletevariant.html',context)