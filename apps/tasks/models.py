from uuid import uuid4

from django.db import models


class Task(models.Model):
    TYPES = (
        ('WEB', 'WEB'),
        ('REVERSE', 'REVERSE'),
        ('STEGO', 'STEGO'),
        ('CRYPTO', 'CRYPTO'),
        ('ADMIN', 'ADMIN'),
        ('JOY', 'JOY'),
        ('FORENSIC', 'FORENSIC'),
        ('PPC', 'PPC')
    )

    uuid = models.UUIDField(primary_key=True, default=uuid4)
    title = models.CharField("Название", max_length=255)
    description = models.TextField("Описание")
    tags = models.CharField(max_length=255, blank=True, null=True)
    type = models.CharField("Тип", choices=TYPES, max_length=255)
    video_url = models.CharField("Ссылка на видео", blank=True, null=True, max_length=255)
    flag = models.CharField("Флаг", max_length=255)
    creator = models.CharField("Создатель", max_length=255, blank=True, null=True)

    class Meta:
        verbose_name = "Задание"
        verbose_name_plural = "Задания"


class SolvedTask(models.Model):
    team = models.ForeignKey("teams.Team", on_delete=models.CASCADE, related_name="solved")
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name="solved")


class TaskFile(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name="files")
    file = models.FileField("Файл")

    class Meta:
        verbose_name = "Файл"
        verbose_name_plural = "Файлы"
