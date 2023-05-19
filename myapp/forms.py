from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from myapp.models import Comment, PersonalPage
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django import forms
from django.contrib.auth import authenticate


class UserCreateForm(UserCreationForm):
    email = forms.EmailField(help_text='A valid email address, please.', required=True)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']


# class UserUpdateForm(forms.ModelForm):
#     email = forms.EmailField()
#
#     class Meta:
#         model = User
#         fields = '__all__'
#
#
# class ProfileUpdateForm(forms.ModelForm):
#     class Meta:
#         model = PersonalPage
#         fields = '__all__'


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