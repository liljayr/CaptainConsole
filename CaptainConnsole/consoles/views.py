from django.http import JsonResponse
from django.shortcuts import get_object_or_404

from common.renderTemplates import renderTemplate
from common.views import sort_items, filter_by_category
from consoles.models import Consoles, ConsoleCategory


def get_console_by_id(request, id):
    return renderTemplate(request, 'consoles/console_details.html', {
        'console': get_object_or_404(Consoles, pk=id)
    })

def index(request):
    if 'search_filter' in request.GET:
        info=Consoles.objects.exclude(description=' ')
        if 'sort_by' in request.GET:
            sort_by = request.GET['sort_by']
            info = sort_items(sort_by, info)
        if 'check' in request.GET:
            consoleCat = request.GET['check']
            info = filter_by_category(consoleCat, info)
        if 'on_sale' in request.GET:
            sale = request.GET['on_sale']
            info = info.filter(onSale=sale)
        info = info.filter(name__icontains=request.GET['search_filter'])
        consoles = [{
            'id': x.id,
            'name': x.name,
            'price': x.price,
            'description': x.description,
            'first_image': x.consoleimage_set.first().image
        } for x in info]
        return JsonResponse({'data': consoles})
    context={'consoles': Consoles.objects.all(), 'categories': ConsoleCategory.objects.all(), 'on_sale': {'On Sale'}}
    return renderTemplate(request, 'consoles/index.html', context)
