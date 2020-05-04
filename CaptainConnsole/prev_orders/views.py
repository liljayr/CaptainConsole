from django.shortcuts import render

prevorders = [
    {'name': 'super mario', 'price': 30},
    {'name': 'tetris', 'price': 17}
]
# Create your views here.
def index(request):
    return render(request, 'prev_orders/index.html', context={'prevorders': prevorders})