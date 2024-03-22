import json
from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import sync_to_async



class ChatConsumer_View(AsyncWebsocketConsumer):
    async def connect(self):
        self.roomGroupName = "group_chat_gfg"
        await self.channel_layer.group_add(
            self.roomGroupName ,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self , close_code):
        await self.channel_layer.group_discard(
            self.roomGroupName, 
            self.channel_name,
        )

    async def receive(self, text_data):
		
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]
        username = text_data_json["username"]
        room_id = text_data_json["room_id"]

        await self.save_message(message, username, room_id)

        await self.channel_layer.group_send(
            self.roomGroupName,{
                "type" : "sendMessage" ,
                "message" : message , 
                "username" : username ,
                "room_id": room_id,
            })

    async def sendMessage(self , event) : 
        message = event["message"]
        username = event["username"]
        await self.send(text_data = json.dumps({"message":message ,"username":username}))

    async def save_message(self, content, username, room_id):
          from chat_room.models import ChatRoomModel
          from main.models import CustomUser
          from message.models import MessageModel

          # Get the CustomUser instance based on the username
          writer = await sync_to_async(CustomUser.objects.get)(username=username)
          # Get the ChatRoomModel instance based on the room_id
          room = await sync_to_async(ChatRoomModel.objects.get)(id=room_id)
          # Save the message to the database
          await sync_to_async(MessageModel.objects.create)(
                content=content,
                writer=writer,
                room=room,
		  )