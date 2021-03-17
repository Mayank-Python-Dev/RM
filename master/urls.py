from django.urls import path


from .import views

from .Views import brand , model , variant , fuel ,colour , form , pricelistview , updatepricelist


urlpatterns = [
    #Dashbpard
    path('', views.dashboard, name='master'),

    #Brand
    path('brands/',brand.brandlist,name = 'brand'),
    path('updatebrand/<str:pk>',brand.updatebrand,name = 'updatebrand'),
    path('deletebrand/<str:pk>',brand.deletebrand,name = 'deletebrand'),

    #Model
    path('models/',model.modellist,name = 'model'),
    path('updatemodel/<str:pk>',model.updatemodel,name = 'updatemodel'),
    path('deletemodel/<str:pk>',model.deletemodel,name = 'deletemodel'),

    #Variant
    path('variants/',variant.variantlist,name = 'variant'),
    path('updatevariant/<str:pk>',variant.updatevariant,name = 'updatevariant'),
    path('deletevariant/<str:pk>',variant.deletevariant,name = 'deletevariant'),

    #Fuel
    path('fuels/',fuel.fuellist,name = 'fuel'),
    path('updatefuel/<str:pk>',fuel.updatefuel,name = 'updatefuel'),
    path('deletefuel/<str:pk>',fuel.deletefuel,name = 'deletefuel'),

    #/Colour
    path('colours/',colour.colourlist,name = 'colour'),
    path('updatecolour/<str:pk>',colour.updatecolour,name = 'updatecolour'),
    path('deletecolour/<str:pk>',colour.deletecolour,name = 'deletecolour'),

    #Pricelist
    path('addpricelist/',form.pricelist,name = 'pricelist'),
    path('pricelist/<str:pk>',pricelistview.Pricelistview,name = 'pricelistview'),
    path('updatepricelist/<str:pk>',updatepricelist.UpdatePriceList,name ='updatepricelist'),

    #for dropdown
    path('ajax/load-models/', views.load_models, name='ajax_load_models'),

]
