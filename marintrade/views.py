from django.shortcuts import render, redirect
from .models import Company, Product, ProductsBlock
from .forms import UserForm, checkCaptcha

def index(request):
    return render(request, 'marintrade/index.html', {'form': UserForm()})

def about(request):
    return render(request, 'marintrade/about.html', {'form': UserForm()})

def vendors(request):
    context = {
        'vendors': Company.objects.all(),
        'form': UserForm()
    }
    return render(request, 'marintrade/vendors.html', context)
def company(request, company_slug):
    company = Company.objects.filter(slug=company_slug)[0]
    productsBlocks = ProductsBlock.objects.filter(company_id = company.id)
    context = {
        'company': company,
        'productsBlocks': productsBlocks,
        'form': UserForm(),
    }
    return render(request, 'marintrade/company.html', context)

def contacts(request):
    return render(request, 'marintrade/contacts.html', {'form': UserForm()})

def questions(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            if checkCaptcha(request, 'question'):
                question = form.save(commit=False)
                question.save()
            else:
                print("Robot")
        else:
            print('Form invalid')
        
        return redirect('/')