from django.db import models


class PartnerOrganization(models.Model):
    tenant = models.ForeignKey('TenantOrganization', on_delete=models.CASCADE, related_name='partners')
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name