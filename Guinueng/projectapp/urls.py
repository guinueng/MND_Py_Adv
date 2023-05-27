from django.urls import path
from projectapp.views import Project_Create_View, Project_Detail_View, Project_List_View

app_name = 'projectapp'

urlpatterns = [
    path('list/', Project_List_View.as_view(), name='list'),
    path('create/', Project_Create_View.as_view(), name='create'),
    path('detail/<int:pk>', Project_Detail_View.as_view(), name='detail'),

]
