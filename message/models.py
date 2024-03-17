from django.db import models
from main.models import CustomUser
from chat_room.models import ChatRoomModel


class MessageModel(models.Model):
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    writer = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    room = models.ForeignKey(ChatRoomModel, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.writer.username} - {self.content}"