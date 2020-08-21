# mysite/routing.py
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
import sockets.routing

application = ProtocolTypeRouter({
    # (http->django views is added by default)
    'websocket': URLRouter(
            sockets.routing.websocket_urlpatterns
    )
  
})