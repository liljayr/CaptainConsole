from django.shortcuts import get_object_or_404

from account.models import *
from common.renderTemplates import renderTemplate





# Create your views here.
def index(request):
    return renderTemplate(request, 'account/login.html')

def get_account_id(request, id):
    context = {'account': get_object_or_404(Accounts, pk=id), 'favorites': Favorites.objects.filter(account_id=id),
               'game': Games.objects.all()}
    return renderTemplate(request, 'account/index.html', context)

def prev_orders(request, id):
    context = {'account': get_object_or_404(Accounts, pk=id), 'orders': Orders.objects.filter(account_id=id, ordered=True)}
    return renderTemplate(request, 'account/prev_orders.html', context)

def edit(request, id):
    context = {'account': get_object_or_404(Accounts, pk=id), 'favorites': Favorites.objects.filter(account_id=id)}
    return renderTemplate(request, 'account/edit.html', context)

def login(request):
    return renderTemplate(request, 'account/login.html')


