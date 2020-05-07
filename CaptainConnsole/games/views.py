from common.renderTemplates import renderTemplate
from games.models import Games

def index(request):
    context = {'games': Games.objects.all().order_by('name')}
    return renderTemplate(request, 'games/index.html', context)
#if doesn't runn turn off db connection in pycharm
def index2(request):
    return renderTemplate(request, 'games/index.html')

