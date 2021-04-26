from django.urls import path


from .import views

from account import views

urlpatterns = [

    path('', views.actdashboard, name='actdashboard'),
    path('paymentregister/<str:pk>/', views.paymentbreakup, name='paymentregistration'),
    path('save/', views.savedata, name='save'),
    path('delete/', views.deletedata, name='delete'),
    path('edit/', views.editdata, name='edit'),

]
