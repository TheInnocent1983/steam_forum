from django.shortcuts import render, get_object_or_404
from .models import Game, Topic


def game_list(request):
    games = Game.objects.all()
    return render(request, "forum/game_list.html", {"games": games})


def game_detail(request, pk):
    game = get_object_or_404(Game, pk=pk)
    return render(request, "forum/game_detail.html", {"game": game})


def topic_detail(request, pk):
    topic = get_object_or_404(Topic, pk=pk)
    return render(request, "forum/topic_detail.html", {"topic": topic})

