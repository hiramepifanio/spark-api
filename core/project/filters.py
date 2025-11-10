import django_filters
from .models import Project

class ProjectFilter(django_filters.FilterSet):
    partner = django_filters.NumberFilter(field_name="partner_id")

    class Meta:
        model = Project
        fields = ["partner"]