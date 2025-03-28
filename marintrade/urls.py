from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('about', about, name='about'),
    path('vendors', vendors, name='vendors'),
    path('vendors/<slug:company_slug>', company, name='company'),
    path('contacts', contacts, name='contacts'),
]
