from django.db import models


class ProjectWorkflow(models.Model):
    tenant = models.ForeignKey('TenantOrganization', on_delete=models.CASCADE, related_name='project_workflows')
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name