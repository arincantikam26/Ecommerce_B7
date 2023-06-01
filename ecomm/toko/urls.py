from django.urls import path
from . import views

app_name = 'toko'

urlpatterns = [
    path('', views.HomeListView, name='home-produk-list'),
    path('shop/', views.ShopView, name='shop'),
    path('contact/', views.ContactView, name='contact'),
]