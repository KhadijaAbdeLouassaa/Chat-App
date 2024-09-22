import json
from channels.generic.websocket import AsyncWebsocketConsumer


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_group_name = "group_chat"
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name,
        )
        await self.accept()
        
    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )
        
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]
        username = text_data_json["username"]
        time = text_data_json["time"]
        thumbnail = text_data_json["thumbnail"]
        await self.channel_layer.group_send(
            self.room_group_name, {
                "type" : "send_message",
                "message" : message,
                "username" : username,
                "time" : time,
                "thumbnail" : thumbnail
            }
        )
        
    async def send_message(self, event):
        message = event["message"]
        username = event["username"]
        time = event["time"]
        thumbnail = event["thumbnail"]
        await self.send(text_data = json.dumps({
            "message" : message,
            "username" : username,
            "time" : time,
            "thumbnail" : thumbnail
        }))
     