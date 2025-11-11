from rest_framework import serializers
from core.project.models import Project

class ProjectListCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = "__all__"
        read_only_fields = ["tenant"]

class ProjectDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = "__all__"
        read_only_fields = ["tenant", "partner"]