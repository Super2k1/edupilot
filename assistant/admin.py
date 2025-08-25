from django.contrib import admin

# Register your models here.
from .models import LeadScore,AssistantSuggestion,SmartMessage

admin.site.register(LeadScore)
admin.site.register(AssistantSuggestion)
admin.site.register(SmartMessage)