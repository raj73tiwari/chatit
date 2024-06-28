from datetime import datetime
from channels.generic.websocket import AsyncWebsocketConsumer
import json
from asgiref.sync import sync_to_async
from . import models

class ChatConsumer(AsyncWebsocketConsumer):

    @sync_to_async
    def get_user_profile(self):
        return self.scope['user'].userprofile
        

    async def connect(self):
        self.room_name=self.scope['url_route']['kwargs']['room_name']
        self.room_group_name=f"chat{self.room_name}"

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self,code):
        
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    
    async def receive(self,text_data):
        data=json.loads(text_data)
        profile = await self.get_user_profile()
        profile_pic = profile.profile_pic.url
        message=data['message']
        room=data['room']
        username = self.scope['user'].username
        timestamp = datetime.now().strftime('%H:%M %d/%m/%y')

        

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chatroom_message',
                'message': message,
                'username': username,
                'profile_pic': profile_pic,
                'room':room,
                'timestamp':timestamp
                
            })
        
        await self.save_msg(self.scope['user'],message,room,timestamp)
        
    async def chatroom_message(self, event):
        message = event['message']
        username = event['username']
        profile_pic = event['profile_pic']
        room=event['room']
        timestamp=event['timestamp']

        await self.send(text_data=json.dumps({
            'message': message,
            'username': username,
            'profile_pic': profile_pic,
            'room':room,
            'timestamp':timestamp
        }))

    @sync_to_async
    def save_msg(self,user,message,room,time):
        room=models.ChatRoom.objects.get(slug=room)
        models.ChatMessage.objects.create(author=user,room=room,message=message,str_time=time)
        


    




            

