from django.urls import path
from core.partner_organization.views import PartnerOrganizationListView, PartnerOrganizationDetailsView

urlpatterns = [
    path('partner-organizations/', PartnerOrganizationListView.as_view(), name='partner-organization-list'),
    path('partner-organizations/<int:pk>/', PartnerOrganizationDetailsView.as_view(), name='partner-organization-details'),
]