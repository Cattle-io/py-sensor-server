# socket/routing.py
from django.urls import re_path

from sockets import consumers

websocket_urlpatterns = [
    re_path(r'ws/sockets/(?P<room_name>\w+)/$', consumers.SocketConsumer),
]