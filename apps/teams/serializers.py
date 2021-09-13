from rest_framework.serializers import ModelSerializer
from apps.teams.models import Team, TeamParticipant
from drf_writable_nested.serializers import WritableNestedModelSerializer


class TeamParticipantSerializer(WritableNestedModelSerializer):
    class Meta:
        model = TeamParticipant
        fields = ('pk', 'name', 'is_captain')


class TeamSerializer(ModelSerializer):
    participants = TeamParticipantSerializer(many=True)

    class Meta:
        model = Team
        fields = ('pk', 'name', 'university', 'team_type', 'score', 'participants')
        read_only_fields = ('score', 'pk')


class TeamCreateSerializer(WritableNestedModelSerializer):
    participants = TeamParticipantSerializer(many=True)

    class Meta:
        model = Team
        fields = ('name', 'password', 'university', 'team_type', 'participants')
