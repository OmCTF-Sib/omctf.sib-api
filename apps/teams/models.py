from django.contrib.auth.models import User
from django.db import models


class Team(models.Model):
    name = models.CharField('Название', max_length=255)
    cap_fio = models.CharField('ФИО Капитана', max_length=255)
    cap_email = models.EmailField('E-mail капитана')
    second_fio = models.CharField('ФИО Участника', max_length=255, blank=True, null=True)
    third_fio = models.CharField('ФИО Участника', max_length=255, blank=True, null=True)
    fourth_fio = models.CharField('ФИО Участника', max_length=255, blank=True, null=True)
    university = models.CharField('ВУЗ', max_length=255)
    pc_count = models.CharField('Кол-во пк', max_length=255)
    type = models.CharField('Тип команды', max_length=255)
    score = models.IntegerField("Кол-во баллов", default=0)
    user = models.OneToOneField(User, verbose_name='Пользователь', related_name="team",
                                on_delete=models.CASCADE, null=True, blank=True)

    login = models.CharField('Логин', max_length=255)
    password = models.CharField('Пароль', max_length=255)

    class Meta:
        verbose_name = 'Команда'
        verbose_name_plural = 'Команды'

    def __str__(self):
        return self.name


class FlagStatistic(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name="statistics")
    flag = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Сданный флаг"
        verbose_name_plural = "Сданные флаги"
