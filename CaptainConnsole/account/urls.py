from django.urls import path
from . import views

urlpatterns = [
    # http://localhost:8000/manufacturers
    path('', views.index, name="account-index"),
    path('prev_orders/', views.prev_orders, name="prev-index"),
    path('edit/', views.edit, name="edit-index"),
    path('login/', views.login, name="login-index")
]