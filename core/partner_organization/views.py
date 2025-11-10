from rest_framework import generics
from core.partner_organization.models import PartnerOrganization
from core.partner_organization.serializers import PartnerOrganizationSerializer


class PartnerOrganizationListView(generics.ListCreateAPIView):
    serializer_class = PartnerOrganizationSerializer

    def get_queryset(self):
        return PartnerOrganization.objects.filter(tenant=self.request.user.tenant)

    def perform_create(self, serializer):
        serializer.save(tenant=self.request.user.tenant)


class PartnerOrganizationDetailsView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PartnerOrganizationSerializer

    def get_queryset(self):
        return PartnerOrganization.objects.filter(tenant=self.request.user.tenant)