from common.renderTemplates import renderTemplate
#from django.shortcuts import render
from django.shortcuts import get_object_or_404

from games.models import Games

def index(request):
    context = {'indi_games': Games.objects.exclude(description=' '), 'games': Games.objects.all()}
    return renderTemplate(request, 'games/index.html', context)
#if doesn't runn turn off db connection in pycharm
#def index2(request):
#    return renderTemplate(request, 'games/index.html')

def get_game_by_id(request, id):
    return renderTemplate(request, 'games/game_details.html', {
        'game': get_object_or_404(Games, pk=id)
    })
