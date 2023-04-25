from django import forms
from myapp.models import Comment
from django.contrib.auth.forms import UserCreationForm


class UserCreateForm(UserCreationForm):
    username = forms.CharField(label='Login', widget=forms.TextInput)
    email = forms.EmailField(widget=forms.EmailInput)
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('text', )