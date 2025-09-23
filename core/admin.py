from django.contrib import admin
from core.models.project import Project

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'started_at', 'finished_at')
