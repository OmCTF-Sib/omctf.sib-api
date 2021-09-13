from django.utils.translation import gettext_lazy as _
from django.db import models
from model_utils.models import TimeStampedModel


class Notification(TimeStampedModel):
    title = models.CharField(_('Title'), max_length=255, blank=True, null=True)
    text = models.TextField(_('Text'), blank=True, null=True)

    is_visible = models.BooleanField(_('Is Visible'), default=True)

    class Meta:
        ordering = ('-created',)
        verbose_name = _('Notification')
        verbose_name_plural = _('Notifications')

    def __str__(self) -> str:
        return self.title
