# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from department.models import Chair, Group

AbstractUser._meta.get_field('email')._unique = True
AbstractUser._meta.get_field('email').blank = False

class Stuff(AbstractUser):
    # Добавляем поле "Фамилия", делаем его обязательным (blank=False)
    surname = models.CharField(_(u'Фамилия'), blank=False, null=True, max_length=100) 
    name = models.CharField(_(u'Имя'), blank=False, null=True, max_length=100) 
    patronymic = models.CharField(_(u'Отчество'), blank=False, null=True, max_length=100)
    # Поле "Логин" делаем уникальным, он и будет ключом
    login = models.CharField(_(u'Логин'), blank=False, null=True, max_length=100, unique=True) 
    # Привязываемся к Chair из department через внешний ключ (не забываем импорт - строка 5) 
    chair = models.ForeignKey(Chair, blank=False, null=True, verbose_name = "Кафедра") 
    class Meta(object):
        verbose_name_plural = "Сотрудники"
        verbose_name = "сотрудника"

class Student(AbstractUser):
    userID = models.CharField(_(u'Номер зачетной книжки'), blank=False, null=True, max_length=100, unique=True)
    login = models.CharField(_(u'Логин'), blank=False, null=True, max_length=100, unique=True) 
    # Здесь ключ формируется из полей userID+login
    surname = models.CharField(_(u'Фамилия'), blank=True, null=True, max_length=100) 
    # Поля Фамилия, Имя и Отчество пока делаем необязательными, для анонимности голосования
    name = models.CharField(_(u'Имя'), blank=True, null=True, max_length=100)
    patronymic = models.CharField(_(u'Отчество'), blank=True, null=True, max_length=100)
    group = models.ForeignKey(Group, blank=False, null=True, verbose_name = "Группа")
    class Meta(object):
        verbose_name_plural = "Студенты"
        verbose_name = "студента"
