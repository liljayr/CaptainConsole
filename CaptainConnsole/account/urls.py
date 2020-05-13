from django.urls import path
from . import views

urlpatterns = [
    # http://localhost:8000/manufacturers
    path('', views.index, name="account-index"),
    path('<int:id>', views.get_account_id, name="account-id-index"),
    path('prev_orders/<int:id>', views.prev_orders, name="prev-index"),
    path('edit/<int:id>', views.edit, name="edit-index"),
#    path('login/', views.login, name="login-index"),
]