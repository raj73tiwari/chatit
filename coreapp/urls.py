from django.urls import path
from . import views

app_name="coreapp"
urlpatterns = [
    path('', views.index, name="index"),
    path('room/<slug:slug>/', views.chat_room, name="room")
]