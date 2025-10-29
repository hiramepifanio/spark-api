from rest_framework import generics
from core.project_workflow.models import ProjectWorkflow
from core.project_workflow.serializers import ProjectWorkflowSerializer


class ProjectWorkflowListView(generics.ListCreateAPIView):
    serializer_class = ProjectWorkflowSerializer

    def get_queryset(self):
        return ProjectWorkflow.objects.filter(organization=self.request.user.organization)

    def perform_create(self, serializer):
        serializer.save(organization=self.request.user.organization)


class ProjectWorkflowDetailsView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProjectWorkflowSerializer

    def get_queryset(self):
        return ProjectWorkflow.objects.filter(organization=self.request.user.organization)