from channels.generic.websocket import AsyncWebsocketConsumer
from .models import MessageModel
from django.core import serializers


# class ChatConsumer_View(AsyncWebsocketConsumer):
#     async def connect(self):
#         await self.accept()

#     async def disconnect(self, close_code):
#         # Perform cleanup tasks here, if necessary
#         await self.close()

#     async def receive(self, text_data):
#         # Process the received message here
#         # For example, you can echo the message back to the client
#         await self.send(text_data=text_data)

class ChatConsumer_View(AsyncWebsocketConsumer):
    async def connect(self):
        # Extract the room ID from the URL
        self.room_id = self.scope['url_route']['kwargs']['id']
        
        # Join a room group based on the room ID
        await self.channel_layer.group_add(
            f"chat_room_{self.room_id}",
            self.channel_name
        )
        
        # Fetch messages from the database for the specified room
        messages = MessageModel.objects.filter(room_id=self.room_id)
        
        # Serialize messages to JSON
        message_data = serializers.serialize('json', messages)
        
        # Send the serialized messages to the client
        await self.send(text_data=message_data)
        
        # Accept the WebSocket connection
        await self.accept()

    async def disconnect(self, close_code):
        # Leave the room group when the WebSocket connection is closed
        await self.channel_layer.group_discard(
            f"chat_room_{self.room_id}",
            self.channel_name
        )

    async def receive(self, text_data):
        # Process received message if needed
        pass