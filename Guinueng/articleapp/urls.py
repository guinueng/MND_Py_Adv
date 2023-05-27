from django.urls import path
from articleapp.views import Article_Create_View, Article_Detail_View, Article_Update_View
from articleapp.views import Article_Delete_View, Article_List_View

app_name = 'articleapp'

urlpatterns = [
    path('list/', Article_List_View.as_view(), name='list'),
    path('create/', Article_Create_View.as_view(), name='create'),
    path('detail/<int:pk>', Article_Detail_View.as_view(), name='detail'),
    path('update/<int:pk>', Article_Update_View.as_view(), name='update'),
    path('delete/<int:pk>', Article_Delete_View.as_view(), name='delete'),

]
