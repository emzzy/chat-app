import os
# import chatapp.routing
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import AllowedHostsOriginValidator
from django.core.asgi import get_asgi_application
import room.routing


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chat_project.settings')

# django_asgi_app = get_asgi_application()

application = ProtocolTypeRouter(
    {
        'http': get_asgi_application(),
        'websocket': AuthMiddlewareStack(
            URLRouter(
                room.routing.websocket_urlpatterns
            )
            #AuthMiddlewareStack(URLRouter(chatapp.routing.websocket_urlpatterns))
        )
    }
)

