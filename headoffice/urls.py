from django.urls import path

from .import views

from .headofficeviews import headoffice
    
urlpatterns = [


    path('', headoffice.Dashboard, name='headoffice'),
    path('approve/<str:pk>/', headoffice.approve, name='approve'),
    path('reject/<str:pk>/', headoffice.reject, name='reject'),
    path('bookingdetails/<str:pk>/',
         headoffice.bookingdetail, name='bookingdetails'),
    path('dealership/', headoffice.dealership, name='HOdealership'),
    # path('modification/<str:pk>/', headoffice.modification, name='modification'),
]
