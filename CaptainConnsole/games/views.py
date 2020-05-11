from django.http import JsonResponse

from common.renderTemplates import renderTemplate
#from django.shortcuts import render
from django.shortcuts import get_object_or_404

from games.models import Games, GameImage

def index(request):
    if 'search_filter' in request.GET:
        search_filter = request.GET['search_filter']
        games = [{
            'id': x.id,
            'name': x.name,
            'description': x.description,
            'price': x.price
            # 'firstImage':x.gameimage_set.first().image
        } for x in Games.objects.filter(name__icontains=search_filter)]
        return JsonResponse({'data': games})
    context = {'indi_games': Games.objects.exclude(description=' '), 'games': Games.objects.all()}
    return renderTemplate(request, 'games/index.html', context)
#if doesn't runn turn off db connection in pycharm
#def index2(request):
#    return renderTemplate(request, 'games/index.html')

def get_game_by_id(request, id):
    return renderTemplate(request, 'games/game_details.html', {
        'game': get_object_or_404(Games, pk=id)
    })
