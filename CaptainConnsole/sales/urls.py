from django.urls import path
from django.shortcuts import render

''' localhost/3000/admin/ '''

def index(request):
    return render(request, 'sales/index.html')