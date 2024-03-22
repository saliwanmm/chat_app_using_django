from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from django.urls import path, re_path

from .consumers import ChatConsumer_View

websocket_urlpatterns = [
    re_path(r"^ws/(?P<id>[^/]+)/$", ChatConsumer_View.as_asgi()),
]

application = ProtocolTypeRouter({
    'websocket': AuthMiddlewareStack(
        URLRouter(
            websocket_urlpatterns
        )
    ),
})