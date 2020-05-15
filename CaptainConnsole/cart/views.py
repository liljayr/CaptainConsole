from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from account.models import Location
from cart.forms.checkout_forms import CheckoutAddressForm, CheckoutCardForm
from common.renderTemplates import renderTemplate
import urllib
import json
from account.models import Order, OrderItems
from django.contrib.auth.models import User
from games.models import Games
from consoles.models import Consoles



@login_required
def index(request):
    return renderTemplate(request, 'cart/index.html')

def checkout_address(request):
    address = Location.objects.filter(user=request.user).first()
    if request.method == 'POST':
        form = CheckoutAddressForm(instance=address, data=request.POST)
        if form.is_valid():
            address = form.save(commit=False)
            address.user = request.user
            address.save()
            return redirect('checkout-card')
    form = CheckoutAddressForm(instance=address)
    return renderTemplate(request, 'cart/checkout.html', {
        'form': form
    })

def checkout_card(request):
    if request.method == 'POST':
        form = CheckoutCardForm(data=request.POST)

        if form.is_valid():
            return redirect('confirmation-index')


    form = CheckoutCardForm()
    return renderTemplate(request, 'cart/checkout_payment.html', {
     'form': form
    })


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
    user_id = request.user.id
    # býr til nýtt order
    user = User.objects.get(id=user_id)
    order = Order(user_id=user)


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
