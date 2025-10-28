from django.urls import path, include

urlpatterns = [
    path('', include('core.project.urls')),
    path('', include('core.stage.urls')),
    path('', include('core.user.urls')),
    path('', include('core.organization.urls')),
]