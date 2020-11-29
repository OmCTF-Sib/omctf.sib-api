from uuid import uuid4

from django.db import models


class News(models.Model):
    title = models.CharField("Заголовок", max_length=255, blank=True, null=True)
    description = models.TextField("Описание", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"


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
    hint = models.TextField("Hint", blank=True, null=True)
    score = models.IntegerField("Кол-во баллов", default=0)
    tags = models.CharField(max_length=255, blank=True, null=True)
    type = models.CharField("Тип", choices=TYPES, max_length=255)
    video_url = models.CharField("Ссылка на видео", blank=True, null=True, max_length=255)
    flag = models.CharField("Флаг", max_length=255)
    creator = models.CharField("Автор", max_length=255, blank=True, null=True)

    class Meta:
        verbose_name = "Задание"
        verbose_name_plural = "Задания"

    def on_save(self):
        old_instance = Task.objects.get(pk=self.pk)
        if old_instance.hint != self.hint:
            News.objects.create(
                title="Добавлена подсказка",
                description=f"К заданию {self.title} ({self.type} - {self.score}) была добавлена подсказка"
            )

    def save(self, *args, **kwargs):
        just_created = False if self.pk else True
        if not just_created:
            self.on_save()

        super(Task, self).save(*args, **kwargs)


class SolvedTask(models.Model):
    team = models.ForeignKey("teams.Team", on_delete=models.CASCADE, related_name="solved")
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name="solved")
    created_at = models.DateTimeField(auto_now_add=True)


class TaskFile(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name="files")
    file = models.FileField("Файл")

    class Meta:
        verbose_name = "Файл"
        verbose_name_plural = "Файлы"
