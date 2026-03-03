from django import forms
from .models import Comment, Game, Topic
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["content"]

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "password1", "password2"]

class GameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = ["name", "description"]

class DeleteForm(forms.Form):
    confirm = forms.BooleanField(
        required=False,
        initial=True,
        widget=forms.HiddenInput
    )


class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ["title"]