from django.shortcuts import render
from django.http import HttpResponse
from accountapp.models import Hello_World

# Create your views here.

def hello_world(request):
	if request.method == "POST":
		temp = request.POST.get('hello_world_input')
		new_hello_world = Hello_World()
		new_hello_world.text = temp
		new_hello_world.save()
		return render(request, 'accountapp/hello_world.html', context = {'hello_world_output': new_hello_world})
	else:
		return render(request, 'accountapp/hello_world.html', context = {'text' : 'GET METHOD!!!'})