from django.urls import path
from profileapp.views import Profile_Create_View, Profile_Update_View

app_name = 'profileapp'

urlpatterns = [
    path('create/', Profile_Create_View.as_view(), name='create'),
    path('update/<int:pk>', Profile_Update_View.as_view(), name='update'),
]