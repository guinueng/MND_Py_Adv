from django.shortcuts import render
from django.urls import reverse
from django.views.generic import CreateView, DetailView, ListView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic.list import MultipleObjectMixin
from projectapp.forms import Project_Creation_Form
from projectapp.models import Project
from articleapp.models import Article
from subscriptionapp.models import Subscription
# Create your views here.


@method_decorator(login_required, 'get')
@method_decorator(login_required, 'post')
class Project_Create_View(CreateView):
    model = Project
    form_class = Project_Creation_Form
    template_name = 'projectapp/create.html'

    def form_valid(self, form):
        temp_project = form.save(commit=False)
        temp_project.writer = self.request.user
        temp_project.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('projectapp:detail', kwargs={'pk': self.object.pk})


class Project_Detail_View(DetailView, MultipleObjectMixin):
    model = Project
    context_object_name = 'target_project'
    template_name = 'projectapp/detail.html'

    paginate_by = 25

    def get_context_data(self, **kwargs):
        project = self.object
        user = self.request.user
        if user.is_authenticated:
            subscription = Subscription.objects.filter(user=user, project=project)
        object_list = Article.objects.filter(project=self.get_object())
        return super(Project_Detail_View, self).get_context_data(
            object_list=object_list, subscription=subscription, **kwargs)


class Project_List_View(ListView):
    model = Project
    context_object_name = 'project_list'
    template_name = 'projectapp/list.html'
    paginate_by = 25
