
from django.urls import path
from .views import show_chat_room_View, creat_room_View, open_room_View


urlpatterns = [
    path("rooms", show_chat_room_View, name="chat_rooms"),
    path("creat_room", creat_room_View, name="creat_room"),
    path("room/<int:id>", open_room_View, name="open_room")
]