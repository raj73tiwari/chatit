from django.shortcuts import render,get_object_or_404
from . import models
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    crooms=models.ChatRoom.objects.all()
    context={'crooms':crooms}
    return render(request,'coreapp/index.html',context)

@login_required
def chat_room(request,slug):
    croom=get_object_or_404(models.ChatRoom, slug=slug)
    messages=models.ChatMessage.objects.filter(room=croom).order_by('-timestamp')[:30]
    context={'croom':croom,'chat_messages':messages}
    return render(request,'coreapp/chat_room.html',context)



