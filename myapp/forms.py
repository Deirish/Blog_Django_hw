from django.forms import ModelForm
from myapp.models import Comment


class CommentForm(ModelForm):

    class Meta:
        model = Comment
        fields = ('text', )