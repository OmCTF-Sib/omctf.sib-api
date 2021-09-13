from django.db import models
from solo.models import SingletonModel
from django.utils.translation import gettext_lazy as _


class SiteSettings(SingletonModel):
    name = models.CharField(_('Competitions name'), default='OmCTF.Sib')
    is_started = models.BooleanField(_('Is Competition Started'), default=False)
    max_participants = models.IntegerField(_('Max Participants in Team'), default=4)

    class Meta:
        verbose_name = _('Site settings')
        verbose_name_plural = _('Site settings')

    def __str__(self) -> str:
        return _('Site settings')
