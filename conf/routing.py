import apps.notifications.routing
from channels.routing import ProtocolTypeRouter, URLRouter

application = ProtocolTypeRouter({
    # (http->django views is added by default)
    'websocket': URLRouter(
        apps.notifications.routing.websocket_urlpatterns
    )
})
