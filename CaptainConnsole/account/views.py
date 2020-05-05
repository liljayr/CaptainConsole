from django.shortcuts import render
from django.http import HttpResponse

favorites = [
    {'name': 'super mario'},
    {'name': 'tetris'}
]

viewed = [
    {'name': 'super mario'},
    {'name': 'tetris'}
]

# Create your views here.
def index(request):
    return render(request, 'account/index.html', context={'favorites': favorites, 'viewed': viewed})

def prev_index(request):
    return render(request, 'account/prev_index.html', context={'favorites': favorites, 'viewed': viewed})
