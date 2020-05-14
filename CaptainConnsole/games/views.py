from django.http import JsonResponse, HttpResponse

from account.models import Favorite
from common.renderTemplates import renderTemplate
from django.shortcuts import get_object_or_404

from consoles.models import Consoles, ConsoleCategory
from games.models import Games


#if doesn't runn turn off db connection in pycharm

def get_game_by_id(request, id):
    return renderTemplate(request, 'games/game_details.html', {
        'game': get_object_or_404(Games, pk=id)
    })

#TODO: add sort by and extra checklist
def index(request):
    if 'search_filter' in request.GET:
        info = Games.objects.all()
        if 'check' in request.GET:
            consoles = request.GET['check']
            if consoles != "":
                for id in consoles.split(','):
                    info = info.filter(console_id=int(id))
        info = info.exclude(description=' ')
        info = info.filter(name__icontains=request.GET['search_filter'])
        print('INFORMATION')
        print(info)
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
               'consoles': ConsoleCategory.objects.all(), 'current_user_id': request.user.id}
    return renderTemplate(request, 'games/index.html', context)

def update_favorites(request):
    if request.method == 'POST':
        #fav = Favorite.objects.get()
        fav = Favorite(game_id='favorite_item', user_id='user_id')
        #fav.game_id = request.POST['favorite_item']
        #fav.user_id = request.POST['user_id']
        fav.save()
        return HttpResponse("kul")