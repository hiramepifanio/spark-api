from django.db import models
import uuid

class Project(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    started_at = models.DateField()
    finished_at = models.DateField(null=True)

    def __str__(self):
        return self.name