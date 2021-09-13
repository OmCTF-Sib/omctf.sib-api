from django.contrib.auth.models import AbstractBaseUser
from django.utils.translation import gettext_lazy as _
from django.db import models
from model_utils import Choices


class Team(AbstractBaseUser):
    USERNAME_FIELD = 'name'
    TEAM_TYPES = Choices(('newbies', _('Newbies')), ('experienced', _('Experienced')))

    name = models.CharField(_('Name'), max_length=255, blank=False, unique=True)
    university = models.CharField(_('University'), max_length=255)
    team_type = models.CharField(_('Command type'), max_length=255, choices=TEAM_TYPES)
    score = models.IntegerField(_('Score'), default=0)

    is_visible = models.BooleanField(_('Is Visible'), default=True)

    class Meta:
        verbose_name = _('Team')
        verbose_name_plural = _('Teams')

    def __str__(self) -> str:
        return self.name


class TeamParticipant(models.Model):
    team = models.ForeignKey(
        Team, verbose_name=_('Team'), on_delete=models.CASCADE, related_name='participants'
    )
    name = models.CharField(_('Name'), max_length=1024, blank=False, null=False)
    is_captain = models.BooleanField(_('Is Captain'), default=False)

    class Meta:
        verbose_name = _('Team participant')
        verbose_name_plural = _('Team participants')

    def __str__(self) -> str:
        return self.name
