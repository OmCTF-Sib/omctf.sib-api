from rest_framework import serializers

from .models import Team


class TeamCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = (
            "name",
            "cap_fio",
            "cap_email",
            "second_fio",
            "third_fio",
            "fourth_fio",
            "university",
            "pc_count",
            "type",
            "login",
            "password",
        )


class TeamListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = (
            'name',
            'type',
            'score'
        )
