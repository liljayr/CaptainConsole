from django.shortcuts import render
from django.http import HttpResponse

games = [
    {'name': 'Super Mario Bros', 'price': 40.99},
    {'name': 'Tetris', 'price': 15.99}
]

# Create your views here.
def index(request):
    return render(request, 'games/index.html', context={
        'games': games
    })

    #return render(request, 'candy/prev_index.html', context={
    #    'candies': candies
    #})
