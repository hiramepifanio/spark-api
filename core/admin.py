from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from core.models import CustomUser
from core.project.models import Project
from core.project_stage.models import ProjectStage
from core.organization.models import Organization
from core.project_workflow.models import ProjectWorkflow


admin.site.register(Organization)
admin.site.register(CustomUser)
admin.site.register(ProjectWorkflow)

@admin.register(ProjectStage)
class ProjectStageAdmin(admin.ModelAdmin):
    list_display = ('id', 'organization', 'project_workflow', 'name', 'order')

# class CustomUserAdmin(UserAdmin):
#     model = CustomUser
#     list_display = ("email", "first_name", "last_name", "is_staff", "is_active")
#     list_filter = ("is_staff", "is_active")
#     search_fields = ("email", "first_name", "last_name")
#     ordering = ("email",)

#     fieldsets = (
#         (None, {"fields": ("email", "password")}),
#         ("Personal Info", {"fields": ("first_name", "last_name")}),
#         ("Permissions", {"fields": ("is_active", "is_staff", "is_superuser", "groups", "user_permissions")}),
#         ("Important dates", {"fields": ("last_login", "date_joined")}),
#     )

#     add_fieldsets = (
#         (None, {
#             "classes": ("wide",),
#             "fields": ("email", "first_name", "last_name", "password1", "password2", "is_staff", "is_active"),
#         }),
#     )


# @admin.register(Project)
# class ProjectAdmin(admin.ModelAdmin):
#     list_display = ('id', 'name', 'description', 'started_at', 'finished_at')


# @admin.register(Stage)
# class StageAdmin(admin.ModelAdmin):
#     list_display = ('id', 'name', 'is_public')
