from django.contrib import admin

# Register your models here.
from .models import LeadSource,  Lead , FollowUp

admin.site.register(LeadSource)
admin.site.register(Lead)   
admin.site.register(FollowUp)
