import json
from channels.generic.websocket import AsyncWebsocketConsumer
from django.contrib.auth.models import User
from .models import Message
from channels.db import database_sync_to_async


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.roomGroupName = "group_chat_gfg"
        await self.channel_layer.group_add(self.roomGroupName, self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.roomGroupName, self.channel_layer)

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]
        username = text_data_json["username"]

        # Userni topish
        user = await self.get_user(username)

        # Yangi habarni yaratish va saqlash
        await self.store_message(user, message)

        await self.channel_layer.group_send(
            self.roomGroupName,
            {
                "type": "send_message",
                "message": message,
                "username": username,
            },
        )

    async def send_message(self, event):
        message = event["message"]
        username = event["username"]
        await self.send(
            text_data=json.dumps({"message": message, "username": username})
        )

    @database_sync_to_async
    def get_user(self, username):
        return User.objects.get(username=username)

    @database_sync_to_async
    def store_message(self, user, message):
        return Message.objects.create(user=user, message=message)
