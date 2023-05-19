from django.urls import path
from accountapp.views import hello_world, Account_Create_View

app_name = "accountapp"

urlpatterns = [
    path('hello_world/', hello_world, name='hello_world'),
    path('create/', Account_Create_View.as_view(), name = 'create'),
]