from django.http import JsonResponse

from common.renderTemplates import renderTemplate
#from django.shortcuts import render
from django.shortcuts import get_object_or_404

from consoles.models import Consoles, ConsoleCategory
from games.models import Games

#if doesn't runn turn off db connection in pycharm
#def index2(request):
#    return renderTemplate(request, 'games/index.html')

def get_game_by_id(request, id):
    return renderTemplate(request, 'games/game_details.html', {
        'game': get_object_or_404(Games, pk=id)
    })

#TODO: add sort by and extra checklist
def index(request):
    if 'search_filter' in request.GET:
        info=Games.objects.exclude(description=' ')
        if 'check' in request.GET:
            consoles = request.GET['check']
            if consoles == "":
                info = info.all()
            else:
                for id in consoles.split(','):
                    info = info.filter(console_id=int(id))
        info = info.filter(name__icontains=request.GET['search_filter'])
        games = [{
            'id': x.id,
            'name': x.name,
            'price': x.price,
            'description': x.description,
            'first_image': x.gameimage_set.first().image
        } for x in info]
        return JsonResponse({'data': games})
    context = {'indi_games': Games.objects.exclude(description=' '), 'games': Games.objects.all(),
               'prices': {'$0.00-$10.00', '$10.01-$15.00', '$15.01-$20.00'},
               'consoles': ConsoleCategory.objects.all()}
    return renderTemplate(request, 'games/index.html', context)