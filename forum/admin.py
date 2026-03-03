from django.contrib import admin
from .models import Game, Topic, Comment


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ["name", "created_at"]


@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ["title", "game", "author", "created_at"]
    list_filter = ["game", "created_at"]


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ["topic", "author", "created_at"]

