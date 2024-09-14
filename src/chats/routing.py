from django.urls import path,include
from chats.consumer import ChatConsumer


websocket_urlpatterns = [
    path('', ChatConsumer.as_asgi())
]