from rest_framework import generics
from core.organization.models import Organization
from core.organization.serializers import OrganizationSerializer


class OrganizationListView(generics.ListCreateAPIView):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer


class OrganizationDetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer