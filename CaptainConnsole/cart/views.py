from common.renderTemplates import renderTemplate


#Dummy data -- replace with connection to database

# Create your views here.
def index(request):
    return renderTemplate(request, 'cart/index.html')

def checkout(request):
    return renderTemplate(request, 'cart/checkout.html')

def confirmation(request):
    return renderTemplate(request, 'cart/confirm.html')

def success(request):
    # Sækja í localStorage
    # Setja í DB
    # Tæma localStorage

    return renderTemplate(request, 'cart/success.html')
