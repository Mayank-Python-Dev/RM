from django.urls import path

from django.conf.urls import include, url

from .import views


urlpatterns = [


    path('', views.loginPage, name='login'),
    # url(r"^accounts/", include("django.contrib.auth.urls")),
    path('logout/', views.logoutPage, name='logout'),

]
