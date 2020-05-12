from django.http import JsonResponse

from common.renderTemplates import renderTemplate
from consoles.models import Consoles

consoles = [
    {'name': 'Nintendo', 'price': 40.99},
    {'name': 'Xbox 1', 'price': 50.99}
]

# Create your views here.
def index(request):
    if 'search_filter' in request.GET:
        search_filter = request.GET['search_filter']
        consoles_results = [{
            'id': x.id,
            'name': x.name,
            'description': x.description,
            'price': x.price
            # 'firstImage':x.gameimage_set.first().image
        } for x in Consoles.objects.filter(name__icontains=search_filter)]
        return JsonResponse({'data': consoles_results})
    return renderTemplate(request, 'consoles/index.html', context={
        'consoles': consoles
    })
