from django.http import JsonResponse
from django.shortcuts import get_object_or_404

from common.renderTemplates import renderTemplate
from consoles.models import Consoles

def get_console_by_id(request, id):
    print("here!")
    print(id)
    return renderTemplate(request, 'consoles/console_details.html', {
        'console': get_object_or_404(Consoles, pk=id)
    })

def index(request):
    context={'consoles': Consoles.objects.all()}
    return renderTemplate(request, 'consoles/index.html', context)
