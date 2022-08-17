"""
ASGI config for jokes_scraper project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter


from jokes.routing import ws_urlpatterns

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'jokes_scraper.settings')

application = ProtocolTypeRouter({
    'http': get_asgi_application(),
    'websocket' : AuthMiddlewareStack(URLRouter(ws_urlpatterns))
})
