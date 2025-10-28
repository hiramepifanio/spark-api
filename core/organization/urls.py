from django.urls import path
from core.organization.views import OrganizationListView, OrganizationDetailsView

urlpatterns = [
    path('organizations/', OrganizationListView.as_view(), name='organization-list'),
    path('organizations/<int:pk>/', OrganizationDetailsView.as_view(), name='organization-details'),
]