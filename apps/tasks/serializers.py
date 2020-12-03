from rest_framework import serializers

from .models import News, Task, TaskFile


class TaskFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskFile
        fields = ('file', )


class TaskSerializer(serializers.ModelSerializer):
    files = TaskFileSerializer(many=True)
    is_solved = serializers.SerializerMethodField()

    class Meta:
        model = Task
        fields = (
            'uuid',
            'title',
            'description',
            'hint',
            'type',
            'tags',
            'creator',
            'video_url',
            'files',
            'score',
            'is_solved',
        )

    @staticmethod
    def get_is_solved(obj):
        return obj.is_solved


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = "__all__"
