from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="games-index"),
    path('<int:id>', views.get_game_by_id, name="game_details"),
    #path('addfavorites', views.update_favorites)
]