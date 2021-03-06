# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _
from accounts.models import Stuff
from department.models import Group, Discipline


# Create your models here.
class Lesson(models.Model):
    group = models.ForeignKey(Group, verbose_name = "Группа")
    discipline = models.ForeignKey(Discipline, verbose_name = "Дисциплина")
    dateAndTtime = models.DateTimeField(_(u'Время и дата'), blank=True, null=True)
    room = models.CharField(max_length=25, blank=False, unique=False, verbose_name=u'Номер аудитории')
    lessonID = models.CharField(_(u'Код занятия'), blank=False, null=True, max_length=100, unique=True)
    status = models.BooleanField(_(u'Статус'), blank=True)
    user = models.ForeignKey(Stuff, blank=False, null=True, verbose_name = "Преподаватель")
    class Meta(object):
        verbose_name_plural = "Занятия"
        verbose_name = "занятие"

