from common.renderTemplates import renderTemplate

from consoles.models import Consoles
from games.models import Games


def index(request):
    consoles = Consoles.objects.filter(onSale=True)
    print("CHECK IT OUT!!!!")
    print(consoles)
    games = Games.objects.filter(onSale=True)
    games = games.exclude(description=' ')
    context = {'consoles': consoles, 'games': games}
    return renderTemplate(request, 'sales/index.html', context)
