from rest_framework import generics
from core.project_workflow.models import ProjectWorkflow
from core.project_stage.models import ProjectStage
from core.project.models import Project
from core.project.serializers import ProjectSerializer
from django.shortcuts import get_object_or_404


class ProjectListView(generics.ListCreateAPIView):
    serializer_class = ProjectSerializer

    def get_queryset(self):
        # return Project.objects.filter(organization=self.request.user.organization)
        return Project.objects.filter(tenant=self.request.user.tenant)

    def perform_create(self, serializer):
        # serializer.save(organization=self.request.user.organization)
        serializer.save(tenant=self.request.user.tenant)


class ProjectDetailsView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProjectSerializer

    def get_queryset(self):
        # return Project.objects.filter(organization=self.request.user.organization)
        return Project.objects.filter(tenant=self.request.user.tenant)


class ProjectListByWorkflowAndStageView(generics.ListAPIView):
    serializer_class = ProjectSerializer

    def get_queryset(self):
        workflow = get_object_or_404(
            ProjectWorkflow,
            pk=self.kwargs["project_workflow_pk"],
            organization=self.request.user.organization
        )
        stage = get_object_or_404(
            ProjectStage,
            pk=self.kwargs["project_stage_pk"],
            project_workflow=workflow,
            organization=self.request.user.organization
        )
        return Project.objects.filter(
            workflow=workflow,
            stage=stage,
            tenant=self.request.user.tenant
        )
