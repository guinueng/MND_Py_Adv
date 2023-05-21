from django.urls import path
from django.views.generic import TemplateView
from articleapp.views import Article_Create_View, Article_Detail_View, Article_Update_View, Article_Delete_View

app_name = 'articleapp'

urlpatterns = [
    path('list/', TemplateView.as_view(template_name='articleapp/list.html'), name='list'),
    path('create/', Article_Create_View.as_view(), name='create'),
    path('detail/<int:pk>', Article_Detail_View.as_view(), name='detail'),
    path('update/<int:pk>', Article_Update_View.as_view(), name='update'),
    path('delete/<int:pk>', Article_Delete_View.as_view(), name='delete'),

]
