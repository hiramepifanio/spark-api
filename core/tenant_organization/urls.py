from django.urls import path
from core.tenant_organization.views import TenantOrganizationListView, TenantOrganizationDetailsView

urlpatterns = [
    path('tenant-organizations/', TenantOrganizationListView.as_view(), name='tenant-organization-list'),
    path('tenant-organizations/<int:pk>/', TenantOrganizationDetailsView.as_view(), name='tenant-organization-details'),
]