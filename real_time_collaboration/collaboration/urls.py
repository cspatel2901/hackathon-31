from django.urls import path
from . import views

urlpatterns = [
    path('chat/<str:room_name>/', views.chat_room, name='chat_room'),
]

urlpatterns = [
    path('chat/<str:room_name>/', views.chat_room, name='chat_room'),
    path('video/<str:room_name>/', views.video_call, name='video_call'),
]