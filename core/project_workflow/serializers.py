from rest_framework import serializers
from core.project_workflow.models import ProjectWorkflow

class ProjectWorkflowSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectWorkflow
        fields = "__all__"
        read_only_fields = ["organization"]