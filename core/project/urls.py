from django.urls import path
from core.project.views import ProjectListView, ProjectDetailsView, ProjectListByWorkflowAndStageView

urlpatterns = [
    path('projects/', ProjectListView.as_view(), name='project-list'),
    path('projects/<int:pk>/', ProjectDetailsView.as_view(), name='project-details'),
    path('project-workflows/<int:project_workflow_pk>/project-stages/<int:project_stage_pk>/projects/', ProjectListByWorkflowAndStageView.as_view(), name='project-list-by-workflow-and-stage'),
]