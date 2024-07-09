# from channels.routing import ProtocolTypeRouter, URLRouter
# from channels.auth import AuthMiddlewareStack
# from django.urls import path
# from chat.consumers import WebConsumer

# application = ProtocolTypeRouter({
#     'websocket':AuthMiddlewareStack(
#         URLRouter([
#             path('ws/<str:id>', WebConsumer.as_asgi()),
#             path('ws/', WebConsumer.as_asgi()),
#         ])
#     )
# })

from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from django.urls import path
from chat.consumers import ChatConsumer

application = ProtocolTypeRouter({
    'websocket': AuthMiddlewareStack(
        URLRouter([
            path('ws/chat/<int:room_id>/', ChatConsumer),
        ])
    ),
})