from django.forms import ModelForm
from profileapp.models import Profile


class Profile_Creation_Form(ModelForm):
    class Meta:
        model = Profile
        fields = ['image', 'nickiname', 'message']
