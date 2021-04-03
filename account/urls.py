from django.urls import path


from .import views


urlpatterns = [

    path('', views.actdashboard, name='actdashboard'),

]
