from rest_framework import viewsets
from core.stage.models import Stage
from core.stage.serializers import StageSerializer

class StageViewSet(viewsets.ModelViewSet):
    queryset = Stage.objects.all()
    serializer_class = StageSerializer