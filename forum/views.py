from django.shortcuts import render, get_object_or_404, redirect
from .models import Game, Topic
from .forms import CommentForm
from .forms import RegisterForm




def game_list(request):
    games = Game.objects.all()
    return render(request, "forum/game_list.html", {"games": games})


def game_detail(request, pk):
    game = get_object_or_404(Game, pk=pk)
    return render(request, "forum/game_detail.html", {"game": game})


def topic_detail(request, pk):
    topic = get_object_or_404(Topic, pk=pk)

    if request.method == "POST":
        if not request.user.is_authenticated:
            return redirect("topic_detail", pk=topic.pk)

        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.topic = topic
            comment.author = request.user
            comment.save()
            return redirect("topic_detail", pk=topic.pk)
    else:
        form = CommentForm()

    return render(request, "forum/topic_detail.html", {
        "topic": topic,
        "form": form
    })

def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = RegisterForm()

    return render(request, "registration/register.html", {"form": form})

