from django.urls import path
from subscriptionapp.views import Subscription_View, Subscription_List_View

app_name = 'subscriptionapp'

urlpatterns = [
    path('subscribe/', Subscription_View.as_view(), name='subscribe'),
    path('list/', Subscription_List_View.as_view(), name='list'),
]
