from django.urls import path
from .views import send_message


urlpatterns = [
    path('message/send/', send_message, name='send_message'),
]