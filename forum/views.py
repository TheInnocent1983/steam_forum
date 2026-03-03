from django.shortcuts import render, get_object_or_404, redirect
from .models import Game, Topic, Comment
from .forms import CommentForm, RegisterForm, GameForm, DeleteForm, TopicForm


def game_list(request):
    games = Game.objects.all()
    delete_form = DeleteForm()
    return render(request, "forum/game_list.html", {"games": games, "delete_form": delete_form})


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
    

def topic_create(request, game_pk):
    game = get_object_or_404(Game, pk=game_pk)

    if not request.user.is_authenticated:
        return redirect("game_detail", pk=game.pk)

    if request.method == "POST":
        form = TopicForm(request.POST)
        if form.is_valid():
            topic = form.save(commit=False)
            topic.game = game
            topic.author = request.user
            topic.save()
            return redirect("topic_detail", pk=topic.pk)
    else:
        form = TopicForm()
    return render(request, "forum/topic_create.html", {"form": form, "game": game})


def topic_edit(request, pk):
    topic = get_object_or_404(Topic, pk=pk)

    if not request.user.is_authenticated or request.user != topic.author:
        return redirect("topic_detail", pk=topic.pk)

    if request.method == "POST":
        form = TopicForm(request.POST, instance=topic)
        if form.is_valid():
            form.save()
            return redirect("topic_detail", pk=topic.pk)
    else:
        form = TopicForm(instance=topic)
    return render(request, "forum/topic_create.html", {"form": form, "topic": topic})


def topic_delete(request, pk):
    topic = get_object_or_404(Topic, pk=pk)

    if not request.user.is_authenticated or request.user != topic.author:
        return redirect("topic_detail", pk=topic.pk)

    if request.method == "POST":
        form = DeleteForm(request.POST)
        if form.is_valid():
            game_pk = topic.game.pk
            topic.delete()
            return redirect("game_detail", pk=game_pk)
    else:
        form = DeleteForm()
    return render(request, "forum/topic_confirm_delete.html", {"form": form, "topic": topic})


def comment_edit(request, pk):
    comment = get_object_or_404(Comment, pk=pk)

    if not request.user.is_authenticated or request.user != comment.author:
        return redirect("topic_detail", pk=comment.topic.pk)

    if request.method == "POST":
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            return redirect("topic_detail", pk=comment.topic.pk)
    else:
        form = CommentForm(instance=comment)
    return render(request, "forum/comment_edit.html", {"form": form, "comment": comment})


def comment_delete(request, pk):
    comment = get_object_or_404(Comment, pk=pk)

    if not request.user.is_authenticated or request.user != comment.author:
        return redirect("topic_detail", pk=comment.topic.pk)

    if request.method == "POST":
        form = DeleteForm(request.POST)
        if form.is_valid():
            topic_pk = comment.topic.pk
            comment.delete()
            return redirect("topic_detail", pk=topic_pk)
    else:
        form = DeleteForm()
    return render(request, "forum/comment_confirm_delete.html", {"form": form, "comment": comment})
    
    
def game_create(request):
    if request.method == "POST":
        form = GameForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("game_list")
    else:
        form = GameForm()
    return render(request, "forum/game_create.html", {"form": form})


def game_edit(request, pk):
    game = get_object_or_404(Game, pk=pk)

    if request.method == "POST":
        form = GameForm(request.POST, instance=game)
        if form.is_valid():
            form.save()
            return redirect("game_detail", pk=game.pk)
    else:
        form = GameForm(instance=game)
    return render(request, "forum/game_edit.html", {"form": form, "game": game})


def game_delete(request, pk):
    game = get_object_or_404(Game, pk=pk)

    if request.method == "POST":
        form = DeleteForm(request.POST)
        if form.is_valid():
            game.delete()
            return redirect("game_list")
    else:
        form = DeleteForm()
    return render(request, "forum/game_confirm_delete.html", {"form": form, "game": game})


def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = RegisterForm()

    return render(request, "registration/register.html", {"form": form})