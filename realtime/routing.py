# routing.py
from channels.routing import route
from .consumers import websocket_receive

channel_routing = [
<<<<<<< HEAD
    route("websocket.receive", websocket_receive, path=r"^/streams/"),
=======
    route("websocket.receive", websocket_receive, path=r"^/chat/"),
>>>>>>> 97623a2bc447b2c27a29f4ffcf4da249df41f661
]
