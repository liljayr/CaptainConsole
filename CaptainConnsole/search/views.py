from django.http import JsonResponse

from common.renderTemplates import renderTemplate
from games.models import Games, GameCategory
from consoles.models import Consoles, ConsoleCategory
from django.contrib.postgres.search import SearchVector

search_results = Games.objects.annotate(search=SearchVector('name')).filter('Tetris')

def index(request):
    if 'search_filter' in request.GET:
        search_filter = request.GET['search_filter']
        products = [{
            'id': x.id,
            'name': x.name,
            'description': x.description
            # 'firstImage':x.gameimage_set.first().image
        } for x in Games.objects.filter(name__icontains=search_filter)]
        return JsonResponse({'data': products})
    return renderTemplate(request, 'search/search.html')




# Create your views here.
