from django.urls import path


from .import views

from account import views

urlpatterns = [

    path('', views.actdashboard, name='actdashboard'),
    path('customer/<str:pk>/',views.customer,name = 'customer'),
    path('payment_register/<str:pk>/',views.createpayment,name ='paymentregister'),
    # path('paymentregister/<str:pk>/', views.paymentbreakup, name='paymentregistration'),
    # path('save/', views.savedata, name='save'),
    # path('delete/', views.deletedata, name='delete'),
    # path('edit/', views.editdata, name='edit'),
    path('updatepayment/<str:pk>/',views.updatepayment,name='update'),
    path('deletepayment/<str:pk>/',views.deletepayment,name='delete'),

]
