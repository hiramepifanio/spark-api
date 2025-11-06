from django.db import models


class ProjectStage(models.Model):
    tenant = models.ForeignKey('TenantOrganization', on_delete=models.CASCADE, related_name='project_stages')
    name = models.CharField(max_length=255)
    project_workflow = models.ForeignKey('ProjectWorkflow', on_delete=models.CASCADE, related_name='stages')
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def save(self, *args, **kwargs):
        if self._state.adding and not self.id:
            last_stage = (
                ProjectStage.objects
                .filter(project_workflow=self.project_workflow)
                .order_by('-order')
                .first()
            )
            self.order = (last_stage.order + 1) if last_stage else 1
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name