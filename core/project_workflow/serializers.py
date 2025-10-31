from rest_framework import serializers
from core.project_workflow.models import ProjectWorkflow
from core.project_stage.serializers import ProjectStageSerializer

class ProjectWorkflowSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectWorkflow
        fields = "__all__"
        read_only_fields = ["organization"]


class ProjectWorkflowDetailSerializer(serializers.ModelSerializer):
    stages = ProjectStageSerializer(many=True, read_only=True)
    
    class Meta:
        model = ProjectWorkflow
        fields = "__all__"
        read_only_fields = ["organization"]