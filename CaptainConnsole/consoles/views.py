from django.shortcuts import render

from django.http import HttpResponse

consoles = [
    {'name': 'Nintendo', 'price': 40.99},
    {'name': 'Xbox 1', 'price': 50.99}
]

# Create your views here.
def index(request):
    return render(request, 'consoles/index.html', context={
        'consoles': consoles
    })
