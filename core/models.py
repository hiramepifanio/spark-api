from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models


class CustomUserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractUser):
    
    class UserRole(models.TextChoices):
        COLLABORATOR = "collaborator", "Collaborator User"
        MANAGER = "manager", "Manager User"
    
    class OrganizationType(models.TextChoices):
        TENANT = "tenant", "Tenant Organization"
        PARTNER = "partner", "Partner Organization"

    username = None
    email = models.EmailField(unique=True)
    tenant = models.ForeignKey('TenantOrganization', on_delete=models.CASCADE, related_name='users', null=True)
    partner = models.ForeignKey('PartnerOrganization', on_delete=models.CASCADE, related_name='users', null=True)
    organization_type = models.CharField(max_length=50, choices=OrganizationType.choices, default=OrganizationType.TENANT)
    role = models.CharField(max_length=50, choices=UserRole.choices, default=UserRole.COLLABORATOR)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    objects = CustomUserManager()

    def __str__(self):
        return self.email