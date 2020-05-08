#from common.renderTemplates import renderTemplate
from django.shortcuts import render

from games.models import Games

def index(request):
    context = {'indi_games': Games.objects.exclude(description=' '), 'games': Games.objects.all()}
    return render(request, 'games/index.html', context)
#if doesn't runn turn off db connection in pycharm
#def index2(request):
#    return renderTemplate(request, 'games/index.html')

