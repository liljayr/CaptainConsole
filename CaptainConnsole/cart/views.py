from django.contrib.auth.decorators import login_required

from common.renderTemplates import renderTemplate
import urllib
import json
from account.models import Order, OrderItems
from django.contrib.auth.models import User
from games.models import Games
from consoles.models import Consoles


#Dummy data -- replace with connection to database

# Create your views here.
@login_required
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
    request_data = u'{}'.format(request.body)
    decoded_data = urllib.parse.unquote(request_data)
    cart_index = decoded_data.find("cart")
    cart_str = decoded_data[cart_index+5:-1]
    cart = json.loads(cart_str)
    print(cart[0])
    user_id = request.user.id
    # býr til nýtt order
    user = User.objects.get(id=user_id)
    order = Order(user_id=user)

    print(user_id)
    order.save()
    for item in cart:
        order_item = OrderItems()
        order_item.order = order
        ids = item["product_id"].split("_")
        _type = ids[0]
        _id = ids[1]
        if _type == "game":
            game = Games.objects.get(id=_id)
            order_item.game_id = game
        else:
            console = Consoles.objects.get(id=_id)
            order_item.console_id = console
        amount = item["amount"]
        order_item.amount = amount
        order_item.save()

    return renderTemplate(request, 'cart/success.html')
