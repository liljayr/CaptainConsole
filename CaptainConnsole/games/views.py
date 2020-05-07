#from renderTemplates import renderTemplate
from django.shortcuts import render

from CaptainConnsole.common.renderTemplates import renderTemplate
from CaptainConnsole.games.models import Games
#or from games.models import Games

def index(request):
    context = {'games': Games.objects.all().order_by('name')}
    return render(request, 'games/index.html', context)
#if doesn't runn turn off db connection in pycharm
def index2(request):
    return render(request, 'games/index.html')
