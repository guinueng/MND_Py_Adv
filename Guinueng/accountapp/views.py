from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DetailView
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from accountapp.models import Hello_World

# Create your views here.

def hello_world(request):
    if request.method=="POST":
        temp=request.POST.get('hello_world_input')

        new_hello_world=Hello_World()
        new_hello_world.text=temp
        new_hello_world.save()

        return HttpResponseRedirect(reverse('accountapp:hello_world'))
    else:
        hello_world_list = Hello_World.objects.all()
        return render(request, 'accountapp/hello_world.html', context={'hello_world_list':hello_world_list})

class Account_Create_View(CreateView):
    model=User
    form_class=UserCreationForm
    success_url=reverse_lazy('accountapp:hello_world')
    template_name='accountapp/create.html'

class Account_Detail_View(DetailView):
    model=User
    context_object_name='target_user'
    template_name='accountapp/detail.html'
