# chat/views.py
from django.shortcuts import render

def index(request):
    return render(request, 'sockets-client.html')

def room(request, room_name):
    return render(request, 'sockets-room.html', {
        'room_name': room_name
})