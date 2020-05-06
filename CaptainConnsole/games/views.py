from django.shortcuts import render
from django.http import HttpResponse

from CaptainConnsole.games.models import Games
#or from games.models import Games

# Create your views here.
def index(request):
    context = {'games': Games.objects.all().order_by('name')}
    return render(request, 'games/index.html', context)
#if doesn't runn turn off db connection in pycharm