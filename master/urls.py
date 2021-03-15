from django.urls import path


from .import views

from .Views import brand , model , variant , fuel ,colour	


urlpatterns = [

    path('', views.dashboard, name='master'),

    path('brands/',brand.brandlist,name = 'brand'),
    path('models/',model.modellist,name = 'model'),
    path('variants/',variant.variantlist,name = 'variant'),
    path('fuels/',fuel.fuellist,name = 'fuel'),
    path('colours/',colour.colourlist,name = 'colour'),

]
