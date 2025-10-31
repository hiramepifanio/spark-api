from rest_framework import serializers
from core.project_stage.models import ProjectStage


class ProjectStageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectStage
        exclude = ['project_workflow']
        read_only_fields = ["organization", "order"]


class ReorderProjectStagesSerializer(serializers.Serializer):
    stage_ids = serializers.ListField(
        child=serializers.IntegerField(),
        allow_empty=False,
        help_text="Ordered list of stage IDs representing the new order."
    )