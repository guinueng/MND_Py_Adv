from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from accountapp.views import hello_world, Account_Create_View

app_name = "accountapp"

urlpatterns = [
    path('hello_world/', hello_world, name='hello_world'),
    
    path('login/', LoginView.as_view(template_name = 'accountapp/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    
    path('create/', Account_Create_View.as_view(), name = 'create'),
]