from django.contrib.auth.models import User
from myapp.models import Comment
from django.contrib.auth.forms import UserCreationForm
from django import forms


class UserCreateForm(UserCreationForm):
    username = forms.CharField(label='Login', widget=forms.TextInput)
    email = forms.EmailField(widget=forms.EmailInput)
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

class CommentForm(forms.Form):
    # text = forms.CharField(max_length=500)
    # author = forms.ModelMultipleChoiceField(queryset=User.objects.all())
    class Meta:
        model = Comment
        fields = ('author', 'text')
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     for field in self.fields:
    #         self.fields[field].widget.attrs['class'] = 'form-control'