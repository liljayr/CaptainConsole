from django.urls import path
from . import views

urlpatterns = [
    # http://localhost:8000/manufacturers
    path('', views.index, name="cart-index"),
    path('checkout/', views.checkout_address, name="checkout-index"),
    path('success/', views.success, name="success-index"),
    path('confirmation', views.confirmation, name="confirmation-index"),
    path('checkout_payment/', views.checkout_card, name="checkout-card")
]