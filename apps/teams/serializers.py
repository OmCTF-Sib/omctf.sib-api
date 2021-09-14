from rest_framework.serializers import ModelSerializer, EmailField
from apps.teams.models import Team, TeamParticipant
from drf_writable_nested.serializers import WritableNestedModelSerializer


class TeamParticipantSerializer(WritableNestedModelSerializer):
    email = EmailField(allow_null=True, allow_blank=False)

    class Meta:
        model = TeamParticipant
        fields = ('pk', 'name', 'email', 'is_captain')


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
        fields = ('name', 'password', 'university', 'team_type', 'participants', 'pc_count')
