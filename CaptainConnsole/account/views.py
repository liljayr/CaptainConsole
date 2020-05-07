from common.renderTemplates import renderTemplate

favorites = [
    {'name': 'super mario'},
    {'name': 'tetris'}
]

viewed = [
    {'name': 'super mario'},
    {'name': 'tetris'}
]

prev_orders = [
    {'name': 'super mario', 'price': 30},
    {'name': 'tetris', 'price': 20}
]

# Create your views here.
def index(request):
    return renderTemplate(request, 'account/index.html', context={'favorites': favorites, 'viewed': viewed})

def prev_orders(request):
    return renderTemplate(request, 'account/prev_orders.html', context={'prev_orders': prev_orders})

def edit(request):
    return renderTemplate(request, 'account/edit.html')


