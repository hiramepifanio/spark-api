from django.db import models

class Project(models.Model):
    
    class InnovationType(models.TextChoices):
        PRODUCT = "product", "Product"
        SERVICE = "service", "Service"
        BUSINESS_PROCESS = "business_process", "Business Process"
        MODEL = "model", "Model"
    
    # class Currency(models.TextChoices):
    #     BRL = "brl", "BRL"
    #     USD = "usd", "USD"

    tenant = models.ForeignKey('TenantOrganization', on_delete=models.CASCADE, related_name='projects')
    partner = models.ForeignKey('PartnerOrganization', on_delete=models.CASCADE, related_name='projects')
    workflow = models.ForeignKey('ProjectWorkflow', null=True, blank=True, on_delete=models.SET_NULL, related_name='projects')
    stage = models.ForeignKey('ProjectStage', null=True, blank=True, on_delete=models.SET_NULL, related_name='projects')
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=255, null=True, blank=True)
    problem = models.CharField(max_length=255, null=True, blank=True)
    benefit = models.CharField(max_length=255, null=True, blank=True)
    innovation_type = models.CharField(max_length=50, choices=InnovationType.choices)
    # cost = models.DecimalField(max_digits=12, decimal_places=2)
    # cost_currency = models.CharField(max_length=50, choices=Currency.choices)
    # duration = models.DurationField()
    cost = models.CharField(max_length=50, null=True, blank=True)
    duration = models.CharField(max_length=50, null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name