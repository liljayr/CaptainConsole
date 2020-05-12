from django.http import JsonResponse

from common.renderTemplates import renderTemplate
#from django.shortcuts import render
from django.shortcuts import get_object_or_404

from games.models import Games

#if doesn't runn turn off db connection in pycharm
#def index2(request):
#    return renderTemplate(request, 'games/index.html')

def get_game_by_id(request, id):
    return renderTemplate(request, 'games/game_details.html', {
        'game': get_object_or_404(Games, pk=id)
    })
def is_valid_queryparam(param):
    return param != '' and param is not None

'''
def filter_view(request):
    info=Games.objects.exclude(description=' ')
    price=request.GET.get('price')
    category=request.GET.get('category')

    if is_valid_queryparam(price) and price == '$0.00-$10.00':
        info = info.filter(price_gte=0.00, price_lte=10.00)
    elif is_valid_queryparam(price) and price != '$10.01-$15.00':
        info = info.filter(price_gte=10.01, price_lte=15.00)
    elif is_valid_queryparam(price) and price != '$15.01-$20.00':
        info = info.filter(price_gte=15.01, price_lte=20.00)

    #if is_valid_queryparam(category):

    return info

    #context = {'indi_games': Games.objects.exclude(description=' '), 'games': Games.objects.all(),
    #           'prices': {'$0.00-$10.00', '$10.01-$15.00', '$15.01-$20.00'}}
'''

def index(request):
    info=Games.objects.exclude(description=' ')
    if 'search_filter' in request.GET:
        search_filter = request.GET['search_filter']
        games = [ {
            'id': x.id,
            'name': x.name,
            'description': x.description,
            'first_image': x.gameimage_set.first().image
        } for x in info.filter(name__icontains=search_filter) ]
        return JsonResponse({'data': games})
    context = {'indi_games': Games.objects.exclude(description=' '), 'games': Games.objects.all(),
               'prices': {'$0.00-$10.00', '$10.01-$15.00', '$15.01-$20.00'}}
    return renderTemplate(request, 'games/index.html', context)