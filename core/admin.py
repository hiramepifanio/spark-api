from django.contrib import admin
from core.project.models import Project
from core.stage.models import Stage

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'started_at', 'finished_at')

@admin.register(Stage)
class StageAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'is_public')
