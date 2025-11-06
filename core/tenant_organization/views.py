from rest_framework import generics
from core.tenant_organization.models import TenantOrganization
from core.tenant_organization.serializers import TenantOrganizationSerializer


class TenantOrganizationListView(generics.ListCreateAPIView):
    queryset = TenantOrganization.objects.all()
    serializer_class = TenantOrganizationSerializer


class TenantOrganizationDetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TenantOrganization.objects.all()
    serializer_class = TenantOrganizationSerializer