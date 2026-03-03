from django.urls import path
from . import views
from .views import register_view


urlpatterns = [
    path("", views.game_list, name="game_list"),
    path("game/<int:pk>/", views.game_detail, name="game_detail"),
    path("topic/<int:pk>/", views.topic_detail, name="topic_detail"),
    path("register/", register_view, name="register"),
]

