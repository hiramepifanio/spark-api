from django.urls import path
from core.project_workflow.views import ProjectWorkflowListView, ProjectWorkflowDetailsView

urlpatterns = [
    path('project-workflows/', ProjectWorkflowListView.as_view(), name='project-workflow-list'),
    path('project-workflows/<int:pk>/', ProjectWorkflowDetailsView.as_view(), name='project-workflow-details'),
]