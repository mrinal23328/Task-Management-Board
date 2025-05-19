from django.contrib import admin
from .models import Task

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'date_of_creation', 'date_of_updation')
    list_filter = ('status',)
    search_fields = ('title', 'description')
