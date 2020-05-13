from django.shortcuts import get_object_or_404, redirect
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

def index(request):
    return renderTemplate(request, 'account/login.html')

def get_account_id(request, id):
    fav_games, fav_consoles = find_fav(id)
    context = {'account': get_object_or_404(Accounts, pk=id), 'game': Games.objects.all(),
               'fav_games': fav_games, 'fav_consoles': fav_consoles}
    return renderTemplate(request, 'account/index.html', context)

def prev_orders(request, id):
    context = {'account': get_object_or_404(Accounts, pk=id), 'orders': Orders.objects.filter(account_id=id, ordered=True)}
    return renderTemplate(request, 'account/prev_orders.html', context)

def edit(request, id):
    fav_games, fav_consoles = find_fav(id)
    context = {'account': get_object_or_404(Accounts, pk=id), 'favorites': Favorites.objects.filter(account_id=id),
               'fav_games': fav_games, 'fav_consoles': fav_consoles}
    return renderTemplate(request, 'account/edit.html', context)

#def profile(request):
#           profile = Accounts.objects.filter(user=request.user).first()
            #-> (ég hef aðgang að innskráðum notanda í gegnum request.user)
#          if request.method == 'POST':  #(breyta eða bæta við profile)
#                form = ProfileForm(instance=profile, data=request.POST)
#                if form._is_valid():
#                    profile = form.save(commit=False)
#                    profile.user = request.user
#                    profile.save()
#                    return redirect('profile')
#               if form._is_valid():
#                  profile = form.save(commit=False)
#                       (ekki búin að bæta þessu profile modeli við í gagnagrunninn,
#                       þetta er tímabundið profile object. Gert því profile þarf
#                       að innihalda foreign key relation á userinn sem ég er ekki búin
#                       að setja.)
#                  profile.user = request.user
#                  profile.save()
#                  return redirect('profile')
#           return renderTemplate(request, 'account.html', {
#               'form': ProfileForm(instance=profile)})