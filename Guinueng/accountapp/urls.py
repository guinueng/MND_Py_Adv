from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from accountapp.views import Account_Create_View, Account_Detail_View
from accountapp.views import Account_Update_View, Account_Delete_View

app_name = "accountapp"

urlpatterns = [
    path('login/', LoginView.as_view(template_name='accountapp/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

    path('create/', Account_Create_View.as_view(), name='create'),
    path('detail/<int:pk>', Account_Detail_View.as_view(), name='detail'),
    path('update/<int:pk>', Account_Update_View.as_view(), name='update'),
    path('delete/<int:pk>', Account_Delete_View.as_view(), name='delete'),
]