from rest_framework import serializers
from rest_framework_recursive.fields import RecursiveField
from project.models import Project
from taggit_serializer.serializers import TagListSerializerField, TaggitSerializer


class ProjectSerializer(TaggitSerializer, serializers.ModelSerializer):
    children = serializers.ListField(read_only=True, source='get_children', child=RecursiveField())
    tags = TagListSerializerField()

    class Meta:
        model = Project
        fields = ['id', 'name', 'type', 'pic', 'tags', 'children']
