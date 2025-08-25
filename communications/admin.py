from django.contrib import admin

# Register your models here.
from .models import Notification,MessageLog,MessageTemplate,Event,Notification
admin.site.register(Notification)
admin.site.register(MessageLog)
admin.site.register(MessageTemplate)
admin.site.register(Event)
