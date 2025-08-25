from django.contrib import admin

# Register your models here.
from .models import School

@admin.register(School)
class SchoolAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'currency', 'created_at']
    list_filter = ['currency', 'created_at']
    search_fields = ['name', 'email']
    readonly_fields = ['created_at', 'updated_at']