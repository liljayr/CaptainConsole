from common.renderTemplates import renderTemplate

favorites = [
    {'name': 'super mario'},
    {'name': 'tetris'},
    {'name': 'super mario'},
    {'name': 'tetris'},
    {'name': 'super mario'},
    {'name': 'tetris'},
    {'name': 'super mario'},
    {'name': 'tetris'}
]

viewed = [
    {'name': 'super mario'},
    {'name': 'tetris'},
    {'name': 'super mario'},
    {'name': 'tetris'},
    {'name': 'super mario'},
    {'name': 'tetris'},
    {'name': 'super mario'},
    {'name': 'tetris'},
    {'name': 'super mario'},
    {'name': 'tetris'}
]

orders = [
    {'name': 'super mario', 'price': 30},
    {'name': 'tetris', 'price': 20},
    {'name': 'super mario', 'price': 30},
    {'name': 'tetris', 'price': 20},
    {'name': 'super mario', 'price': 30},
    {'name': 'tetris', 'price': 20},
    {'name': 'super mario', 'price': 30},
    {'name': 'tetris', 'price': 20},
    {'name': 'super mario', 'price': 30},
    {'name': 'tetris', 'price': 20}
]

# Create your views here.
def index(request):
    return renderTemplate(request, 'account/index.html', context={'favorites': favorites, 'viewed': viewed})

def prev_orders(request):
    return renderTemplate(request, 'account/prev_orders.html', context={'orders': orders})

def edit(request):
    return renderTemplate(request, 'account/edit.html', context={'favorites': favorites, 'viewed': viewed})

def login(request):
    return renderTemplate(request, 'account/login.html')


