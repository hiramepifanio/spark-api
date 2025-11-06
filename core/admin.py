from django.contrib import admin
from core.models import CustomUser
from core.project_stage.models import ProjectStage
from core.tenant_organization.models import TenantOrganization
from core.partner_organization.models import PartnerOrganization
from core.project_workflow.models import ProjectWorkflow
from core.project.models import Project


@admin.register(TenantOrganization)
class TenantOrganizationAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(PartnerOrganization)
class PartnerOrganizationAdmin(admin.ModelAdmin):
    list_display = ('id', 'tenant', 'name')


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'tenant', 'email', 'first_name')


@admin.register(ProjectWorkflow)
class ProjectWorkflowAdmin(admin.ModelAdmin):
    list_display = ('id', 'tenant', 'name')


@admin.register(ProjectStage)
class ProjectStageAdmin(admin.ModelAdmin):
    list_display = ('id', 'tenant', 'project_workflow', 'name', 'order')


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'tenant', 'workflow', 'stage', 'name', 'is_active')
