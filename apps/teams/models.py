from django.apps import apps
from django.contrib.auth.hashers import make_password
from typing import Any, Optional
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.utils.translation import gettext_lazy as _
from django.db import models
from model_utils import Choices


class TeamManager(BaseUserManager):
    def _create_user(self, name: str, password: Optional[str], **extra_fields: Any):
        if not name:
            raise ValueError('The given name must be set')

        user_model = apps.get_model(self.model._meta.app_label, self.model._meta.object_name)
        name = user_model.normalize_username(name)
        user = self.model(name=name, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, name: str, password: Optional[str] = None, **extra_fields: Any):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(name, password, **extra_fields)

    def create_superuser(self, name: str, password: Optional[str] = None, **extra_fields: Any):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(name, password, **extra_fields)


class Team(AbstractBaseUser):
    USERNAME_FIELD = 'name'
    TEAM_TYPES = Choices(('newbies', _('Newbies')), ('experienced', _('Experienced')))

    name = models.CharField(_('Name'), max_length=255, blank=False, unique=True)
    university = models.CharField(_('University'), max_length=255)
    team_type = models.CharField(_('Command type'), max_length=255, choices=TEAM_TYPES)
    score = models.IntegerField(_('Score'), default=0)

    is_visible = models.BooleanField(_('Is Visible'), default=True)
    is_staff = models.BooleanField(_('Is Staff'), default=False)
    is_superuser = models.BooleanField(_('Is Superuser'), default=False)

    objects = TeamManager()

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
