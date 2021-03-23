from django.urls import path


from .import views

from .headofficeviews import headoffice

urlpatterns = [


	path('', headoffice.Dashboard, name = 'headoffice'),
]