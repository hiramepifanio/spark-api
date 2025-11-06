from rest_framework import serializers
from core.tenant_organization.models import TenantOrganization

class TenantOrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = TenantOrganization
        fields = "__all__"