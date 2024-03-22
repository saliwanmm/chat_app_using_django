from django.shortcuts import redirect, render

from message.models import MessageModel
from .models import ChatRoomModel


def show_chat_room_View(request):
    chats = ChatRoomModel.objects.all().order_by("-id")
    return render(request, "chats/chat_rooms.html", {
        "chats": chats,
    })


def creat_room_View(request):
    if request.method == "POST":
        new_chat_room = ChatRoomModel.objects.create()
        new_chat_room.title = request.POST.get("title")
        new_chat_room.description = request.POST.get("description")
        new_chat_room.save()
        return redirect("/chat/rooms")
    else:
        return render(request, "chats/create_chat_rooms.html")
    

def open_room_View(request, id):
    room_id = ChatRoomModel.objects.get(id=id).id
    messages = MessageModel.objects.filter(room=ChatRoomModel.objects.get(id=id))
    context = {"id":id, "room_id": room_id, "messages": messages}
    return render(request, "chats/room.html", context)
