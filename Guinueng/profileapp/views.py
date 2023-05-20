from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
from profileapp.models import Profile
from profileapp.forms import Profile_Creation_Form
# Create your views here.

class Profile_Create_View(CreateView):
    model = Profile
    context_object_name = 'target_profile'
    form_class = Profile_Creation_Form
    success_url = reverse_lazy('accountapp:hello_world')
    template_name = 'profileapp/create.html'
    
    def form_valid(self, form):
        temp_profile = form.save(commit=False)
        temp_profile.user = self.request.user
        temp_profile.save()
        return super().form_valid(form)