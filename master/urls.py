from django.urls import path


from .import views

from .Views import brand, model, variant, fuel, colour, form, pricelistview, updatepricelist, dealership, register


urlpatterns = [
    # Dashboard
    path('', views.dashboard, name='master'),
    path('deletedeal/<str:pk>', views.deletedeal, name='deletedeal'),

    # Brand
    path('brands/', brand.brandlist, name='brand'),
    path('updatebrand/<str:pk>', brand.updatebrand, name='updatebrand'),
    path('deletebrand/<str:pk>', brand.deletebrand, name='deletebrand'),

    # Model
    path('models/', model.modellist, name='model'),
    path('updatemodel/<str:pk>', model.updatemodel, name='updatemodel'),
    path('deletemodel/<str:pk>', model.deletemodel, name='deletemodel'),

    # Variant
    path('variants/', variant.variantlist, name='variant'),
    path('updatevariant/<str:pk>', variant.updatevariant, name='updatevariant'),
    path('deletevariant/<str:pk>', variant.deletevariant, name='deletevariant'),

    # Fuel
    path('fuels/', fuel.fuellist, name='fuel'),
    path('updatefuel/<str:pk>', fuel.updatefuel, name='updatefuel'),
    path('deletefuel/<str:pk>', fuel.deletefuel, name='deletefuel'),

    # /Colour
    path('colours/', colour.colourlist, name='colour'),
    path('updatecolour/<str:pk>', colour.updatecolour, name='updatecolour'),
    path('deletecolour/<str:pk>', colour.deletecolour, name='deletecolour'),

    # Pricelist
    path('addpricelist/', form.pricelist, name='pricelist'),
    path('pricelist/<str:pk>', pricelistview.Pricelistview, name='pricelistview'),
    path('updatepricelist/<str:pk>',
         updatepricelist.UpdatePriceList, name='updatepricelist'),

    # for dropdown
    path('ajax/load-models/', views.load_models, name='ajax_load_models'),
    path('ajax/load-fuels/', views.load_fuels, name='ajax_load_fuels'),
    path('ajax/load-variants/', views.load_variants, name='ajax_load_variants'),
    path('ajax/load-colours/', views.load_colours, name='ajax_load_colours'),


    # dealership
    path('dealership/', dealership.createdealership, name='dealership'),
    path('selectgroups/', register.select_groups, name='groups'),
    path('selectgroups/sales', register.register_sales, name='registersales'),
    path('selectgroups/headoffice', register.register_headoffice,
         name='registerheadoffice'),
    path('dealershipview/', register.dealership, name='dealershipview'),
    path('selectgroups/EDP', register.register_edp, name='registeredp'),
    path('selectgroups/account', register.register_account, name='registeraccount'),


]
