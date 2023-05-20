from django.urls import path
from profileapp.views import Profile_Create_View

app_name = 'profileapp'

urlpatterns = [
    path('create/', Profile_Create_View.as_view(), name='create'),
]