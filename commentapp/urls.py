from django.urls import path
from commentapp.views import Comment_Create_View, Comment_Delete_View
app_name = 'commentapp'

urlpatterns = [
    path('create/', Comment_Create_View.as_view(), name='create'),
    path('delete/<int:pk>', Comment_Delete_View.as_view(), name='delete'),

]
