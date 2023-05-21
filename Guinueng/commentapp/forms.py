from django.forms import ModelForm
from commentapp.models import Comment


class Comment_Creation_Form(ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
