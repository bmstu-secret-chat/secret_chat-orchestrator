import json
import websockets
from channels.generic.websocket import AsyncWebsocketConsumer


class MessengerProxyConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        await self.send(text_data="connect")
        self.realtime_websocket = await websockets.connect("ws://localhost:8002/messenger/")
    
    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data):
        data = {"message": text_data}
        await self.realtime_websocket.send(json.dumps(data))
        response = await self.realtime_websocket.recv()
        await self.send(text_data=f"Ответ от микросервиса: {response}")
