from uuid import uuid4
from django.utils.translation import gettext_lazy as _
from django.db import models
from model_utils.models import TimeStampedModel
from apps.teams.models import Team


class TaskType(models.Model):
    name = models.CharField(_('Name'), max_length=255)

    class Meta:
        verbose_name = _('Task type')
        verbose_name_plural = _('Task types')

    def __str__(self) -> str:
        return self.name


class Task(TimeStampedModel):
    uuid = models.UUIDField(primary_key=True, default=uuid4)
    name = models.CharField(_('Name'), max_length=255)
    description = models.TextField(_('Description'))
    score = models.IntegerField(_('Score'), default=0)
    type = models.ForeignKey(
        TaskType, verbose_name=_('Task type'), on_delete=models.CASCADE, related_name='tasks'
    )

    tags = models.CharField(
        _('Tags'), max_length=255, blank=True, null=True, help_text=_('Separated by commas')
    )
    hint = models.TextField('Hint', blank=True, null=True)

    url = models.CharField(_('URL'), blank=True, null=True, max_length=255)

    creator = models.CharField(_('Creator'), max_length=255, blank=True, null=True)

    is_visible = models.BooleanField(_('Is Visible'), default=True)

    class Meta:
        verbose_name = _('Task')
        verbose_name_plural = _('Tasks')

    def __str__(self) -> str:
        return self.name


class TaskFile(models.Model):
    task = models.ForeignKey(
        Task, verbose_name=_('Task'), on_delete=models.CASCADE, related_name='files'
    )
    file = models.FileField(_('File'))

    class Meta:
        verbose_name = _('File')
        verbose_name_plural = _('Files')

    def __str__(self) -> str:
        return self.file.name


class SolvedTask(TimeStampedModel):
    team = models.ForeignKey(
        'teams.Team', verbose_name=_('Team'), on_delete=models.CASCADE, related_name='solved'
    )
    task = models.ForeignKey(
        Task, verbose_name=_('Task'), on_delete=models.CASCADE, related_name='solved'
    )

    class Meta:
        verbose_name = _('Solved task')
        verbose_name_plural = _('Solved tasks')

    def __str__(self) -> str:
        return self.task.name


class FlagStatistic(TimeStampedModel):
    team = models.ForeignKey(
        Team, verbose_name=_('Team'), on_delete=models.CASCADE, related_name='statistics'
    )
    flag = models.CharField(max_length=255, verbose_name=_('Flag'), blank=True, null=True)

    class Meta:
        verbose_name = _('Sent flag')
        verbose_name_plural = _('Sent flags')

    def __str__(self) -> str:
        return self.flag
