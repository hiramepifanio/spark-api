from rest_framework import serializers
from core.partner_organization.models import PartnerOrganization

class PartnerOrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = PartnerOrganization
        fields = "__all__"
        read_only_fields = ['tenant']