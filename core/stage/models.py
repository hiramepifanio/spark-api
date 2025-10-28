from django.db import models
import uuid

class Stage(models.Model):
    name = models.CharField(max_length=50)
    is_public = models.BooleanField(default=False)

    def __str__(self):
        return self.name