from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from core.models import CustomUser
from core.project.models import Project
from core.stage.models import Stage
from core.organization.models import Organization


admin.site.register(Organization)
admin.site.register(CustomUser)

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
