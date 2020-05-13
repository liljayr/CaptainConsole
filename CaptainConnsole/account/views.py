from django.shortcuts import get_object_or_404, redirect

from account.models import *
from common.renderTemplates import renderTemplate
from account.forms.account_form import EditAccountForm, EditImageForm

def get_search_history(id_val):
    history = SearchHistory.filter(user_id=id_val)
    game_history = history.filter(category='games')
    console_history = history.filter(category='consoles')
    return game_history, console_history

def find_fav(id):
    fav = Favorite.objects.filter(user_id=id)
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
    orders = Order.objects.filter(user_id=id, ordered=True)
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
    game_history, console_history = get_search_history(id)
    context = {'account': get_object_or_404(User, pk=id), 'game': Games.objects.all(),
               'fav_games': fav_games, 'fav_consoles': fav_consoles,
               'game_history': game_history, 'console_history': console_history}
    return renderTemplate(request, 'account/index.html', context)

def prev_orders(request, id):
    game_orders, console_orders = find_orders(id)
    context = {'account': get_object_or_404(User, pk=id), 'game_orders': game_orders,
               'console_orders': console_orders}
    return renderTemplate(request, 'account/prev_orders.html', context)

def edit(request, id):
    fav_games, fav_consoles = find_fav(id)
    account = get_object_or_404(User, pk=id)
    image = ProfileImage.objects.all().filter(user=id).first()

    if request.method == 'POST':
        form = EditAccountForm(data=request.POST, instance=account)
        img_form = EditImageForm(data=request.POST, instance=image)
        if form.is_valid() and img_form.is_valid():
            account = form.save()
            img = img_form.save()
            profile_image = ProfileImage(image=request.POST['image'], account=account)
            profile_image.save()
            return redirect('account-id-index', id=id)
    else:
        form = EditAccountForm(instance=account)
        img_form = EditImageForm(instance=image)
    context = {'account': account, 'fav_games': fav_games, 'fav_consoles': fav_consoles,
               'form': form, 'id': id, 'img_form': img_form}
    return renderTemplate(request, 'account/edit.html', context)

def login(request):
    return renderTemplate(request, 'account/login.html')


