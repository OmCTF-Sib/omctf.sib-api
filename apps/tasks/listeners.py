from typing import Any, Set
from django.db.models.signals import post_save
from django.dispatch.dispatcher import receiver
from apps.tasks.models import Task, SolvedTask
from apps.notifications.models import Notification
from django.utils.translation import gettext_lazy as _


@receiver(post_save, sender=Task)
def task_model_post_save(
    instance: Task, created: bool, update_fields: Set, *args: Any, **kwargs: Any
) -> None:
    if 'hint' in update_fields:
        Notification.objects.create(
            title=_('New hint'),
            text=_(
                'A hint was added to the task: %(task)s (%(task_type)s - {%(task_score)s})'
                % {
                    'task': instance.name,
                    'task_type': instance.type.name,
                    'task_score': instance.score,
                }
            ),
        )


@receiver(post_save, sender=SolvedTask)
def solved_task_model_post_save(
    instance: SolvedTask, created: bool, *args: Any, **kwargs: Any
) -> None:
    if created and not SolvedTask.objects.filter(task=instance.task).exists():
        Notification.objects.create(
            title=_('First blood'),
            text=_(
                'Team: %(team)s made first blood on %(task)s'
                % {'team': instance.team.name, 'task': instance.task.name}
            ),
        )
