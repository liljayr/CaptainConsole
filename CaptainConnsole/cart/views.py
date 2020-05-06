from django.shortcuts import render
from django.http import HttpResponse


#Dummy data -- replace with connection to database
cart = [
    {'name': 'Super Mario Bros', 'amount': 1, 'price': 30.00},
    {'name': 'Tetris', 'amount': 1, 'price': 40.00}
]
total_price = 0
for item in range(len(cart)):
    total_price += cart[item].get('price')

# Create your views here.
def index(request):
    return render(request, 'cart/index.html', context={ 'cart' : cart, 'total_price' : total_price })

def checkout(request):
    return render(request, 'cart/checkout.html')

def success(request):
    return render(request, 'cart/success.html')
