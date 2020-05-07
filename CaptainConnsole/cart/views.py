from common.renderTemplates import renderTemplate


#Dummy data -- replace with connection to database
cart = [
    {'name': 'Super Mario Bros', 'amount': 1, 'price': 30.00},
    {'name': 'Tetris', 'amount': 1, 'price': 40.00}
]
total_price = 0
num_in_cart = len(cart)
for item in range(len(cart)):
    total_price += cart[item].get('price')

# Create your views here.
def index(request):
    return renderTemplate(request, 'cart/index.html', context={ 'cart' : cart, 'total_price' : total_price })

def checkout(request):
    return renderTemplate(request, 'cart/checkout.html', context={  'cart' : cart, 'total_price' : total_price ,'num_in_cart' : num_in_cart})

def confirmation(request):
    return renderTemplate(request, 'cart/confirmation.html', context={  'cart' : cart, 'total_price' : total_price, 'num_in_cart' : num_in_cart})

def success(request):
    return renderTemplate(request, 'cart/success.html')
