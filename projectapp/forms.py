from django.forms import ModelForm
from projectapp.models import Project


class Project_Creation_Form(ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'image', 'description']
