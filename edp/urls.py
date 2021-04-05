from django.urls import path


from .import views

from .edpviews import payment

urlpatterns = [

    path('', views.edpdashboard, name='edpdashboard'),
    path('paymentbreakup/', payment.edppayment, name='paymentbreakup'),

]
