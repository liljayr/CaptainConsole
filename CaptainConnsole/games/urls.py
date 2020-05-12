from django.urls import path
from . import views

urlpatterns = [
    # http://localhost:8000/manufacturers
    path('', views.index, name="games-index"),
    path('<int:id>', views.get_game_by_id, name="game_details")
    #path('', views.filter_view, name="price")
]