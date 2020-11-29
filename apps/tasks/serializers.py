from rest_framework import serializers

from .models import Task, TaskFile


class TaskFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskFile
        fields = ('file', )


class TaskSerializer(serializers.ModelSerializer):
    files = TaskFileSerializer(many=True)

    class Meta:
        model = Task
        fields = (
            'uuid',
            'title',
            'description',
            'type',
            'tags',
            'creator',
            'video_url',
            'files'
        )
