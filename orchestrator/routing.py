from django.urls import path
from realtime.consumers import MessengerProxyConsumer

websocket_urlpatterns = [
    path('messenger/', MessengerProxyConsumer.as_asgi()),
]
