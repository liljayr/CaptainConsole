from django.urls import path
from . import views

urlpatterns = [
    # http://localhost:8000/manufacturers
    path('', views.index, name="cart-index"),
    path('checkout/', views.checkout, name="checkout-index"),
    path('success/', views.success, name="success-index"),
    path('confirmation', views.confirmation, name="confirmation-index")
]