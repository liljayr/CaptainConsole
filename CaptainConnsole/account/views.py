from django.shortcuts import get_object_or_404

from account.models import *
from common.renderTemplates import renderTemplate

def find_fav(id):
    fav = Favorites.objects.filter(account_id=id)
    fav_games = []
    fav_consoles = []
    for prod in fav:
        try:
            if prod.game_id:
                fav_games.append(prod)
        except:
            if prod.console_id:
                fav_consoles.append(prod)
    return fav_games, fav_consoles

def find_orders(id):
    orders = Orders.objects.filter(account_id=id, ordered=True)
    game_orders = []
    console_orders = []
    for ord in orders:
        try:
            if ord.game_id:
                game_orders.append(ord)
        except:
            if ord.console_id:
                console_orders.append(ord)
    return game_orders, console_orders

# Create your views here.
def index(request):
    return renderTemplate(request, 'account/login.html')

def get_account_id(request, id):
    fav_games, fav_consoles = find_fav(id)
    context = {'account': get_object_or_404(Accounts, pk=id), 'game': Games.objects.all(),
               'fav_games': fav_games, 'fav_consoles': fav_consoles}
    return renderTemplate(request, 'account/index.html', context)

def prev_orders(request, id):
    game_orders, console_orders = find_orders(id)
    context = {'account': get_object_or_404(Accounts, pk=id), 'game_orders': game_orders, 'console_orders': console_orders}
    return renderTemplate(request, 'account/prev_orders.html', context)

def edit(request, id):

    fav_games, fav_consoles = find_fav(id)
    context = {'account': get_object_or_404(Accounts, pk=id), 'favorites': Favorites.objects.filter(account_id=id),
               'fav_games': fav_games, 'fav_consoles': fav_consoles}
    return renderTemplate(request, 'account/edit.html', context)

def login(request):
    return renderTemplate(request, 'account/login.html')


