from django.contrib import admin

from . import models

# Register your models here.

admin.site.register(models.ChatRoom)
admin.site.register(models.ChatMessage)

