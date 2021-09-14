from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.contrib.auth.forms import UserCreationForm as BaseUserCreationForm

from apps.teams.models import Team


class TeamAdminForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField(
        label='Пароль', help_text="<a href='../password/'>Сменить пароль</a>"
    )

    def clean_password(self) -> str:
        return self.initial['password']


class TeamCreationForm(BaseUserCreationForm):
    class Meta(BaseUserCreationForm):
        model = Team
        fields = ('name',)
