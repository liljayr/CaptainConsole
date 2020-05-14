from django.http import JsonResponse
from django.shortcuts import get_object_or_404

from common.renderTemplates import renderTemplate
from consoles.models import Consoles

def get_console_by_id(request, id):
    return renderTemplate(request, 'consoles/console_details.html', {
        'console': get_object_or_404(Consoles, pk=id)
    })

def index(request):
    if 'search_filter' in request.GET:
        info=Consoles.objects.exclude(description=' ')
        if 'check' in request.GET:
            consoleCat = request.GET['check']
            if consoleCat == "":
                info = info.all()
            else:
                for id in consoleCat.split(','):
                    info = info.filter(console_id=int(id))
        info = info.filter(name__icontains=request.GET['search_filter'])
        consoles = [{
            'id': x.id,
            'name': x.name,
            'price': x.price,
            'description': x.description,
            'first_image': x.consoleimage_set.first().image
        } for x in info]
        return JsonResponse({'data': consoles})
    context={'consoles': Consoles.objects.all()}
    return renderTemplate(request, 'consoles/index.html', context)
