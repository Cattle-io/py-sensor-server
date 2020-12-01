from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
import sockets.routing

from sockets.consumers import PacketsSocketsConsumer


application = ProtocolTypeRouter({
    'websocket': URLRouter([
        path('ws/packets/<slug:chatname>/', PacketsSocketsConsumer),
    ])
})


