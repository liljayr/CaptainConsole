from django.shortcuts import render
from django.http import HttpResponse

candies = [
    {'name': 'smartis', 'price': 4.99},
    {'name': 'skittles', 'price': 5.99}
]

# Create your views here.
def index(request):
    return render(request, 'games/index.html')

    #return render(request, 'candy/prev_orders.html', context={
    #    'candies': candies
    #})
