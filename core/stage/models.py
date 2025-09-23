from django.db import models
import uuid

class Stage(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50)
    is_public = models.BooleanField(default=False)

    def __str__(self):
        return self.name