from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from myapp.models import Comment
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django import forms
from django.contrib.auth import authenticate


class UserCreateForm(UserCreationForm):
    email = forms.EmailField(help_text='A valid email address, please.', required=True)
    # username = forms.CharField(label='Login', widget=forms.TextInput)
    # email = forms.EmailField(widget=forms.EmailInput)
    # password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    # password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

    # def save(self, commit=True):
    #     user = super(UserCreateForm, self).save(commit=False)
    #     user.email = self.cleaned_data['email']
    #     if commit:
    #         user.save()
    #     return user

    # def clean(self):
    #     cleaned_data = super().clean()
    #     username = cleaned_data.get('username')
    #     password2 = cleaned_data.get('password2')
    #     email = cleaned_data.get('email')
    #     if username and password2:
    #         self.user = authenticate(username=username, password2=password2, email=email)
    #         if self.user is None:
    #             raise forms.ValidationError('OOPS!!!')


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