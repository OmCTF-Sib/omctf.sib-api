from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from django.core import exceptions as django_exceptions
from apps.teams.models import Team, TeamParticipant
from django.db import IntegrityError, transaction
from drf_writable_nested.serializers import WritableNestedModelSerializer


class TeamParticipantSerializer(WritableNestedModelSerializer):
    email = serializers.EmailField(allow_null=True, allow_blank=False)

    class Meta:
        model = TeamParticipant
        fields = ('pk', 'name', 'email', 'is_captain')


class TeamSerializer(serializers.ModelSerializer):
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

    def validate(self, attrs: dict) -> dict:
        team = Team(**attrs)
        password = attrs.get('password')

        try:
            validate_password(password, team)
        except django_exceptions.ValidationError as e:
            serializer_error = serializers.as_serializer_error(e)
            raise serializers.ValidationError({'password': serializer_error['non_field_errors']})

        return attrs

    def create(self, validated_data: dict) -> Team:
        try:
            team = self.perform_create(validated_data)
        except IntegrityError:
            self.fail('cannot_create_user')

        return team

    def perform_create(self, validated_data: dict) -> Team:
        with transaction.atomic():
            user = Team.objects.create_user(**validated_data)
        return user
