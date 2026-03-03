from django.urls import path
from . import views
from .views import register_view


urlpatterns = [
    path("", views.game_list, name="game_list"),
    path("game/<int:pk>/", views.game_detail, name="game_detail"),
    path("game/create/", views.game_create, name="game_create"),
    path("game/<int:pk>/edit/", views.game_edit, name="game_edit"),
    path("game/delete/<int:pk>/", views.game_delete, name="game_delete"),
    path("topic/<int:pk>/", views.topic_detail, name="topic_detail"),
    path("game/<int:game_pk>/topic/create/", views.topic_create, name="topic_create"),
    path("topic/<int:pk>/edit/", views.topic_edit, name="topic_edit"),
    path("topic/<int:pk>/delete/", views.topic_delete, name="topic_delete"),
    path("comment/<int:pk>/edit/", views.comment_edit, name="comment_edit"),
    path("comment/<int:pk>/delete/", views.comment_delete, name="comment_delete"),
    path("register/", register_view, name="register"),
]

