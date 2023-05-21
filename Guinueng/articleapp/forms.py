from django.forms import ModelForm
from articleapp.models import Article


class Article_Creation_Form(ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'image', 'content']
