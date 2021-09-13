from typing import Any
from rest_framework import serializers

from .models import Task, TaskFile


class TaskFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskFile
        fields = ('file',)


class TaskListSerializer(serializers.ModelSerializer):
    is_solved = serializers.SerializerMethodField()

    class Meta:
        model = Task
        fields = ('uuid', 'name', 'description', 'type', 'tags', 'score', 'is_solved')

    @staticmethod
    def get_is_solved(obj: Any) -> bool:
        return obj.is_solved


class TaskDetailSerializer(serializers.ModelSerializer):
    files = TaskFileSerializer(many=True)
    is_solved = serializers.SerializerMethodField()

    class Meta:
        model = Task
        fields = (
            'uuid',
            'name',
            'description',
            'type',
            'tags',
            'score',
            'is_solved',
            'files',
            'url',
            'creator',
        )

    @staticmethod
    def get_is_solved(obj: Any) -> bool:
        return obj.is_solved


class SendFlagSerializer(serializers.Serializer):
    flag = serializers.CharField(required=True)
