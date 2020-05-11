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
def is_valid_queryparam(param):
    return param != '' and param is not None

def filter_view(request):
    price=request.GET.get('price')
    category=request.GET.get('category')

    if is_valid_queryparam(price) and price > 0.00 and price < 8.00:
        Games.objects.filter(price_gte=0.00, price_lte=8.00)

    #if is_valid_queryparam(category):