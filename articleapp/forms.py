from django.forms import ModelForm
from django import forms
from articleapp.models import Article
from projectapp.models import Project


class Article_Creation_Form(ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={'class': 'editable',
                                                           'style': 'height: auto; text-align: left;'}))

    project = forms.ModelChoiceField(queryset=Project.objects.all(), required=False)
    class Meta:
        model = Article
        fields = ['title', 'project', 'image', 'content']
