from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.views.generic.list import MultipleObjectMixin
from django.utils.decorators import method_decorator
from accountapp.forms import Account_Update_Form
from accountapp.decorators import account_ownership_required
from articleapp.models import Article
# Create your views here.
has_ownership = [account_ownership_required, login_required]


class Account_Create_View(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('accountapp:detail')
    template_name = 'accountapp/create.html'


class Account_Detail_View(DetailView, MultipleObjectMixin):
    model = User
    context_object_name = 'target_user'
    template_name = 'accountapp/detail.html'

    paginate_by = 25

    def get_context_data(self, **kwargs):
        object_list = Article.objects.filter(writer=self.get_object())
        return super(Account_Detail_View, self).get_context_data(object_list=object_list, **kwargs)


class Account_Update_View(UpdateView):
    model = User
    context_object_name = 'target_user'
    form_class = Account_Update_Form
    success_url = reverse_lazy('accountapp:detail')
    template_name = 'accountapp/update.html'


@method_decorator(has_ownership, 'get')
@method_decorator(has_ownership, 'post')
class Account_Delete_View(DeleteView):
    model = User
    context_object_name = 'target_user'
    success_url = reverse_lazy('accountapp:login')
    template_name = 'accountapp/delete.html'
