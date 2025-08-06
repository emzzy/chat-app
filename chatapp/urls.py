from django.urls import path
from . import views

urlpatterns = [
    path('chat/', views.index, name='index'),
    path('chat/<str:room_name>/', views.room, name='room'),
    path('stream_webhook/', views.stream_webhook, name='stream_webhook'),
]