from django.urls import path
from . import views

''' localhost/3000/admin/ '''

urlpatterns = [
    path('', views.index, name="home-index")
]