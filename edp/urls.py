from django.urls import path


from .import views

from .edpviews import dashboard , payment

urlpatterns = [

    path('', dashboard.edpdashboard, name='edpdashboard'),
    path('paymentbreakup/', payment.edppayment, name='paymentbreakup'),
    path('generate_DMS&Tally/<str:pk>/',dashboard.edpform,name = 'DMS&Tally')

]
