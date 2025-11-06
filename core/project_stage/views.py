from rest_framework import generics, status
from core.project_workflow.models import ProjectWorkflow
from core.project_stage.models import ProjectStage
from core.project_stage.serializers import ProjectStageSerializer, ProjectStageDetailSerializer, ReorderProjectStagesSerializer
from django.shortcuts import get_object_or_404
from rest_framework.response import Response

class ProjectStageListView(generics.ListCreateAPIView):
    serializer_class = ProjectStageSerializer

    def get_queryset(self):
        project_workflow = get_object_or_404(
            ProjectWorkflow,
            pk=self.kwargs["project_workflow_pk"],
            tenant=self.request.user.tenant
        )

        return ProjectStage.objects.filter(
            project_workflow=project_workflow,
            tenant=self.request.user.tenant
        )

    def perform_create(self, serializer):
        project_workflow = get_object_or_404(
            ProjectWorkflow,
            pk=self.kwargs["project_workflow_pk"],
            tenant=self.request.user.tenant
        )

        serializer.save(
            tenant=self.request.user.tenant,
            project_workflow=project_workflow
        )


class ProjectStageDetailsView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProjectStageDetailSerializer

    def get_queryset(self):
        return ProjectStage.objects.filter(
            tenant=self.request.user.tenant,
            project_workflow__pk=self.kwargs["project_workflow_pk"]
        )


class ReorderProjectStagesView(generics.GenericAPIView):
    serializer_class = ReorderProjectStagesSerializer

    def patch(self, request, project_workflow_pk):
        workflow = get_object_or_404(
            ProjectWorkflow,
            pk=project_workflow_pk,
            tenant=request.user.tenant
        )
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        stage_ids = serializer.validated_data["stage_ids"]

        stages = ProjectStage.objects.filter(project_workflow=workflow)

        workflow_stage_ids = set(stages.values_list("id", flat=True))
        if set(stage_ids) - workflow_stage_ids:
            return Response (
                {"detail": "Some stage IDs do not belong to this workflow."},
                status=status.HTTP_400_BAD_REQUEST
            )

        for order, stage_id in enumerate(stage_ids, start=1):
            ProjectStage.objects.filter(id=stage_id).update(order=order)

        return Response (
            {"detail": "Stages reordered successfully."},
            status=status.HTTP_200_OK
        )