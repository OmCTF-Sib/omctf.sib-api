from django.db import models


class Team(models.Model):
    name = models.CharField('Название', max_length=255)
    cap_fio = models.CharField('ФИО Капитана', max_length=255)
    cap_email = models.EmailField('E-mail капитана')
    university = models.CharField('ВУЗ', max_length=255)
    pc_count = models.CharField('Кол-во пк', max_length=255)
    type = models.CharField('Тип команды', max_length=255)
    login = models.CharField('Логин', max_length=255)
    password = models.CharField('Пароль', max_length=255)

    class Meta:
        verbose_name = 'Команда'
        verbose_name_plural = 'Команды'
