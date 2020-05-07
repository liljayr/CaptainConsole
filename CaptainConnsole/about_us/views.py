from django.shortcuts import render

from renderTemplates import renderTemplate

def index(request):
    return render(request, 'about_us/index.html')
