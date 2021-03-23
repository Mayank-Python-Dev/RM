from django.shortcuts import render, redirect




def Dashboard(request):
	context = {}
	return render(request,'headoffice/headofficedashboard.html',context)