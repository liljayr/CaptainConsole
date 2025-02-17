from django.http import JsonResponse, HttpResponse

from account.models import Favorite
from django.contrib.auth.models import User

from account.models import SearchHistory
from common.renderTemplates import renderTemplate
from django.shortcuts import get_object_or_404

from common.views import sort_items, filter_by_category, add_favorite, search_history
from consoles.models import ConsoleCategory
from games.models import Games, GameCategory


#if doesn't run turn off db connection in pycharm





def get_game_by_id(request, id):
    return renderTemplate(request, 'games/game_details.html', {
        'game': get_object_or_404(Games, pk=id)
    })

def index(request):
    if 'search_filter' in request.GET:
        user_id = request.user.id
        if user_id != None:
            search_history(user_id, request.GET['hidden'], request.GET['search_filter'])
            if 'prod_id' in request.GET:
                add_favorite(user_id, request.GET['hidden'], request.GET['prod_id'])
        info = Games.objects.all()
        if 'sort_by' in request.GET:
            sort_by = request.GET['sort_by']
            info = sort_items(sort_by, info)
        if 'check' in request.GET:
            consoles = request.GET['check']
            if consoles != "":
                for id in consoles.split(','):
                    info = info.filter(console_id=int(id))
        if 'type' in request.GET:
            typeCat = request.GET['type']
            info = filter_by_category(typeCat, info)
        if 'on_sale' in request.GET:
            sale = request.GET['on_sale']
            if sale == 'True':
                info = info.filter(onSale=sale)
        info = info.exclude(description=' ')
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
               'consoles': ConsoleCategory.objects.all(), 'current_user_id': request.user.id, 'on_sale': {'On Sale'},
               'types': GameCategory.objects.all()}
    return renderTemplate(request, 'games/index.html', context)


