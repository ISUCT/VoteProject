# -*- coding=utf8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _

class Faculty(models.Model):
    name = models.CharField(max_length=200,unique=True,verbose_name=u'Имя факультета')
    def __unicode__(self):
        return self.name
    class Meta(object):
        verbose_name_plural = "Факультеты"
        verbose_name = "факультет"

class Chair(models.Model):
    name = models.CharField(max_length=200,unique=True,verbose_name=u'Имя кафедры')
    faculty = models.ForeignKey(Faculty)
    def __unicode__(self):
        return self.name
    class Meta(object):
        verbose_name_plural = "Кафедры"
        verbose_name = "кафедру"

class Course (models.Model):
    name = models.CharField(max_length=200,unique=True,verbose_name=u'Номер курса')
    def __unicode__(self):
        return self.name
    class Meta(object):
        verbose_name_plural = "Курсы"
        verbose_name = "курс"

class Discipline (models.Model):
    name = models.CharField(max_length=200,unique=True,verbose_name=u'Название дисциплины')
    course = models.ForeignKey(Course)
    chair = models.ForeignKey(Chair)
    def __unicode__(self):
        return self.name
    class Meta(object):
        verbose_name_plural = "Дисциплины"
        verbose_name = "дисциплину"

class Group(models.Model):
    name = models.CharField(max_length=200,unique=True,verbose_name=u'Номер группы')
    course = models.ForeignKey(Course)
    def __unicode__(self):
        return self.name
    class Meta(object):
        verbose_name_plural = "Группы"
        verbose_name = "группу"





