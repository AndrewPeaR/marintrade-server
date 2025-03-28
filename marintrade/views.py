from django.shortcuts import render
from .models import Product

def index(request):
    return render(request, 'marintrade/index.html')

def about(request):
    return render(request, 'marintrade/about.html')

def vendors(request):
    return render(request, 'marintrade/vendors.html')

def contacts(request):
    return render(request, 'marintrade/contacts.html')