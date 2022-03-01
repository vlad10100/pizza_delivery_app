from django.urls import path 

from authentication.views import UserCreationView


app_name='authentication'

urlpatterns = [
    path('signup/', UserCreationView.as_view(), name='user-creation'),
]
