from django.urls import path
from core.project_stage.views import ProjectStageListView, ProjectStageDetailsView, ReorderProjectStagesView

urlpatterns = [
    path('project-workflows/<int:project_workflow_pk>/project-stages/', ProjectStageListView.as_view(), name='project-stage-list'),
    path('project-workflows/<int:project_workflow_pk>/project-stages/<int:pk>/', ProjectStageDetailsView.as_view(), name='project-stage-details'),
    path('project-workflows/<int:project_workflow_pk>/reorder-stages/', ReorderProjectStagesView.as_view(), name='project-workflow-reorder-stages'),
]