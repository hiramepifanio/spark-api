from rest_framework.routers import DefaultRouter
from core.stage.views import StageViewSet

router = DefaultRouter()
router.register(r'stages', StageViewSet, basename='stage')

urlpatterns = router.urls