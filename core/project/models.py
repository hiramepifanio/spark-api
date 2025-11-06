from django.db import models

class Project(models.Model):
    tenant = models.ForeignKey('TenantOrganization', on_delete=models.CASCADE, related_name='projects')
    partner = models.ForeignKey('PartnerOrganization', on_delete=models.CASCADE, related_name='projects')
    workflow = models.ForeignKey('ProjectWorkflow', null=True, blank=True, on_delete=models.SET_NULL, related_name='projects')
    stage = models.ForeignKey('ProjectStage', null=True, blank=True, on_delete=models.SET_NULL, related_name='projects')
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name