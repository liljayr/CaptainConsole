from django.shortcuts import get_object_or_404, redirect
from account.models import *
from cart.forms.checkout_forms import CheckoutAddressForm
from common.renderTemplates import renderTemplate
from account.forms.account_form import EditAccountForm, EditImageForm

def get_search_history(id_val):
    game_history = []
    console_history = []
    history = SearchHistory.objects.all().filter(user=id_val)
    for search in history:
        if search.value != "" and search.value != "undefined":
            if search.category == "games":
                game_history.append(search.value)
            if search.category == "consoles":
                console_history.append(search.value)
    return game_history, console_history

def find_fav(id):
    fav = Favorite.objects.filter(user_id=id)
    fav_games = []
    fav_consoles = []
    for prod in fav:
        if prod.game_id != -1:
            g_id = prod.game_id
            game = Games.objects.all().filter(pk=g_id)
            if game.first() != None:
                fav_games.append(game.first())
            else:
                if prod.console_id != -1:
                    c_id = prod.console_id
                    console = Consoles.objects.all().filter(pk=c_id)
                    fav_consoles.append(console.first())
    return fav_games, fav_consoles

# Create your views here.
def index(request):
    return renderTemplate(request, 'account/login.html')

def get_account_id(request, id):
    img = ProfileImage.objects.all().filter(user=id).first().image
    fav_games, fav_consoles = find_fav(id)
    game_history, console_history = get_search_history(id)
    context = {'account': get_object_or_404(User, pk=id), 'game': Games.objects.all(),
               'fav_games': fav_games, 'fav_consoles': fav_consoles,
               'game_history': game_history, 'console_history': console_history, 'profile_image': img}
    return renderTemplate(request, 'account/index.html', context)

def edit(request, id):
    img = ProfileImage.objects.all().filter(user=id).first().image
    fav_games, fav_consoles = find_fav(id)
    account = get_object_or_404(User, pk=id)
    image = ProfileImage.objects.all().filter(user=id).first()

    if request.method == 'POST':
        form = EditAccountForm(data=request.POST, instance=account)
        img_form = EditImageForm(data=request.POST, instance=image)
        if form.is_valid() and img_form.is_valid():
            account = form.save()
            img = img_form.save()
            profile_image = ProfileImage(image=request.POST['image'], user=account)
            profile_image.save()
            return redirect('account-id-index', id=id)
    else:
        form = EditAccountForm(instance=account)
        img_form = EditImageForm(instance=image)
    context = {'account': account, 'fav_games': fav_games, 'fav_consoles': fav_consoles,
               'form': form, 'id': id, 'img_form': img_form, 'profile_image': img}
    return renderTemplate(request, 'account/edit.html', context)


