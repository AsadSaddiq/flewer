from django.contrib import admin
from chat.models import Contact, Message

# # Register your models here.
# admin.site.register(Message)

class chatapp(admin.ModelAdmin):
    list_display = ('id', 'sender', 'receiver', 'message')
admin.site.register(Message, chatapp)

class contact(admin.ModelAdmin):
    list_display = ('id', 'sender_id', 'receiver_id', 'img')
admin.site.register(Contact, contact)