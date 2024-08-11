from django.shortcuts import render

# Create your views here.
def chat_room(request, room_name):
    return render(request, 'chat.html', {
        'room_name': room_name
    })

def video_call(request, room_name):
    return render(request, 'video_call.html', {
        'room_name': room_name
    })