from rest_framework import generics
from core.project_workflow.models import ProjectWorkflow
from core.project_workflow.serializers import ProjectWorkflowSerializer, ProjectWorkflowDetailSerializer


class ProjectWorkflowListView(generics.ListCreateAPIView):
    serializer_class = ProjectWorkflowSerializer

    def get_queryset(self):
        return ProjectWorkflow.objects.filter(tenant=self.request.user.tenant)

    def perform_create(self, serializer):
        serializer.save(tenant=self.request.user.tenant)


class ProjectWorkflowDetailsView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProjectWorkflowDetailSerializer

    def get_queryset(self):
        return ProjectWorkflow.objects.filter(tenant=self.request.user.tenant)