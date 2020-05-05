from django.urls import path
from . import views

urlpatterns = [
    # http://localhost:8000/manufacturers
    path('', views.index, name="account-index"),
    path('prev_orders/', views.index2, name="prev-index"),
]