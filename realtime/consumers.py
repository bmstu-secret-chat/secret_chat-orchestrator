import asyncio
import websockets
from channels.generic.websocket import AsyncWebsocketConsumer


class MessengerProxyConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        print("connect")
        await self.send(text_data="connect")
        # self.realtime_websocket = await websockets.connect('ws://localhost:8001/')
    
    async def disconnect(self, close_code):
        # await self.realtime_websocket.close()
        pass

    async def receive(self, text_data):
        await self.send(text_data=text_data)
        await asyncio.sleep(5)
        await self.send(text_data=f"Возвращаем сообщение: {text_data}")
        # response = await self.realtime_websocket.recv()
        # await self.send(text_data=response)
