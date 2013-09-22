# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from department.models import Chair, Group

AbstractUser._meta.get_field('email')._unique = True
AbstractUser._meta.get_field('email').blank = False

class Stuff(AbstractUser):
    # Добавляем поля . null=True не нужен т.к. в БД это обычное текстовое поле.
    # max_length=1000 - по умолчанию значение 100, пару раз натыкался на глюки при длинных названиях файлов,
    # может в 1.5 уже и не нужно, но там все так же 100.
    #! avatar = models.ImageField(_(u'avatar'), upload_to='accounts/avatar/%Y/%m/', blank=True, max_length=1000)
    # Добавляем поле дня рождения.
    #! birthday = models.DateField(_(u'birthday'), blank=True, null=True)
    surname = models.CharField(_(u'Фамилия'), blank=True, null=True, max_length=100)
    name = models.CharField(_(u'Имя'), blank=True, null=True, max_length=100)
    patronymic = models.CharField(_(u'Отчество'), blank=True, null=True, max_length=100)
    login = models.CharField(_(u'Логин'), blank=False, null=True, max_length=100, unique=True)
    #password = models.DateField(_(u'password'), blank=True, null=True)
    # Привязываемся к Chair из department через внешний ключ
    chair = models.ForeignKey(Chair, blank=False, null=True, verbose_name = "Кафедра")
    class Meta(object):
        verbose_name_plural = "Сотрудники"
        verbose_name = "сотрудника"

class Student(AbstractUser):
    userID = models.CharField(_(u'Номер зачетной книжки'), blank=False, null=True, max_length=100, unique=True)
    login = models.CharField(_(u'Логин'), blank=False, null=True, max_length=100, unique=True)
    surname = models.CharField(_(u'Фамилия'), blank=True, null=True, max_length=100)
    name = models.CharField(_(u'Имя'), blank=True, null=True, max_length=100)
    patronymic = models.CharField(_(u'Отчество'), blank=True, null=True, max_length=100)
    group = models.ForeignKey(Group, blank=False, null=True, verbose_name = "Группа")
    class Meta(object):
        verbose_name_plural = "Студенты"
        verbose_name = "студента"
