from rest_framework import generics
from core.partner_organization.models import PartnerOrganization
from core.partner_organization.serializers import PartnerOrganizationSerializer


class PartnerOrganizationListView(generics.ListCreateAPIView):
    queryset = PartnerOrganization.objects.all()
    serializer_class = PartnerOrganizationSerializer


class PartnerOrganizationDetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PartnerOrganization.objects.all()
    serializer_class = PartnerOrganizationSerializer