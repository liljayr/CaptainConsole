from django.urls import path
from . import views

urlpatterns = [
    # http://localhost:8000/manufacturers
    path('', views.index, name="account-index"),
    # http://localhost:8000/manufacturers
    path('', views.prev_index, name="prev-index"),
]