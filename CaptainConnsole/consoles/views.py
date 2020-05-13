from django.http import JsonResponse

from common.renderTemplates import renderTemplate
from consoles.models import Consoles

consoles = [
    {'name': 'Nintendo', 'price': 40.99},
    {'name': 'Xbox 1', 'price': 50.99}
]

# Create your views here.
def index(request):
    return renderTemplate(request, 'consoles/index.html', context={
        'consoles': Consoles.objects.all()
    })
