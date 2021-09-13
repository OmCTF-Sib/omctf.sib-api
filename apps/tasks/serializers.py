from typing import Any
from rest_framework import serializers

from .models import Task, TaskFile, TaskType


class TaskFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskFile
        fields = ('file',)


class TaskTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskType
        fields = ('name',)


class TaskListSerializer(serializers.ModelSerializer):
    is_solved = serializers.SerializerMethodField()
    type = TaskTypeSerializer()

    class Meta:
        model = Task
        fields = ('uuid', 'name', 'description', 'type', 'tags', 'score', 'is_solved')

    @staticmethod
    def get_is_solved(obj: Any) -> bool:
        return obj.is_solved


class TaskDetailSerializer(serializers.ModelSerializer):
    files = TaskFileSerializer(many=True)
    is_solved = serializers.SerializerMethodField()
    type = TaskTypeSerializer()

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
