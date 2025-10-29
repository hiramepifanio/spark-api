from django.db import models


class ProjectWorkflow(models.Model):
    organization = models.ForeignKey('Organization', on_delete=models.CASCADE, related_name='project_workflows')
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name