from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="account-index"),
    path('<int:id>', views.get_account_id, name="account-id-index"),
    path('edit/<int:id>', views.edit, name="edit-index"),
]