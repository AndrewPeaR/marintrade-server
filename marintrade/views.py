from django.shortcuts import render
from .models import Company

def index(request):
    return render(request, 'marintrade/index.html')

def about(request):
    return render(request, 'marintrade/about.html')

def vendors(request):
    context = {
        'vendors': Company.objects.all()
    }
    return render(request, 'marintrade/vendors.html', context)
def company(request, company_slug):
    # print(Company.objects.filter(slug=company_slug))
    context = {
        'company': Company.objects.filter(slug=company_slug)[0]
    }
    return render(request, 'marintrade/company.html', context)

def contacts(request):
    return render(request, 'marintrade/contacts.html')