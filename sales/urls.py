from django.urls import path


from .import views

from .SalesViews import sales

urlpatterns = [

	path('',sales.Dashboard,name = 'sales'),
	path('booking/',sales.Booking, name = 'booking'),
	path('addbooking/',sales.Booking, name = 'booking'),
	path('option/',sales.DropdownData, name = 'option'),
	path('detail/',sales.Detail, name = 'detail'),
	path('updatebooking/<str:pk>',sales.updatebooking,name ='updatebooking'),
	path('deletebooking/<str:pk>',sales.deletebooking,name ='deletebooking'),

]