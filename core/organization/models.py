from django.db import models


class Organization(models.Model):
    
    class OrganizationRole(models.TextChoices):
        PARTNER = "partner", "Partner Organization"
        ADMIN = "admin", "Admin Organization"

    name = models.CharField(max_length=255)
    role = models.CharField(max_length=50, choices=OrganizationRole.choices)

    def __str__(self):
        return self.name