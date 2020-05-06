from renderTemplates import renderTemplate

onSale = [
    {'name': 'Super Mario Bros', 'price': 4.99},
]

# Create your views here.
def index(request):
    return renderTemplate(request, 'sales/index.html', context={
        'onSale': onSale
    })
