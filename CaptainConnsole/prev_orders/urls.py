from django.urls import path
from . import views

urlpatterns = [
    # http://localhost:8000/prev_orders
    path('', views.index, name="prev_orders-index"),
]