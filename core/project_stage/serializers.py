from rest_framework import serializers
from core.project_stage.models import ProjectStage
from core.project.serializers import ProjectListCreateSerializer


class ProjectStageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectStage
        fields = '__all__'
        read_only_fields = ["tenant", "order", 'project_workflow']


class ProjectStageDetailSerializer(serializers.ModelSerializer):
    projects = ProjectListCreateSerializer(many=True, read_only=True)

    class Meta:
        model = ProjectStage
        fields = '__all__'
        read_only_fields = ["tenant", "order", 'project_workflow']


class ReorderProjectStagesSerializer(serializers.Serializer):
    stage_ids = serializers.ListField(
        child=serializers.IntegerField(),
        allow_empty=False,
        help_text="Ordered list of stage IDs representing the new order."
    )