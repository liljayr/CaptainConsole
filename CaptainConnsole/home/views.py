from django.shortcuts import render
from django.http import HttpResponse

candies = [
    {'name': 'smartis', 'price': 4.99},
    {'name': 'skittles', 'price': 5.99}
]

# Create your views here.
def index(request):
    return HttpResponse('the hoooome site!')

