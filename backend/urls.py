from django.urls import path
from .views import get_chats


urlpatterns = [
    path('get/', get_chats, name='get_chats'),
]