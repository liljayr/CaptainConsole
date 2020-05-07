from django.shortcuts import render

from renderTemplates import renderTemplate

onSale = [
    {'name': 'Super Mario Bros', 'price': 4.99},
]

# Create your views here.
def index(request):
    return render(request, 'sales/index.html', context={
        'onSale': onSale
    })
