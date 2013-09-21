# -*- coding=utf8 -*-
from django.db import models

class Faculty(models.Model):
    name = models.CharField(max_length=200,unique=True,verbose_name=u'Имя факультета')
    def __unicode__(self):
        return self.name

class Chair(models.Model):
    name = models.CharField(max_length=200,unique=True,verbose_name=u'Имя кафедры')
    faculty = models.ForeignKey(Faculty)
    def __unicode__(self):
        return self.name

class Course (models.Model):
    name = models.CharField(max_length=200,unique=True,verbose_name=u'Number of course')
    def __unicode__(self):
        return self.name

class Discipline (models.Model):
    name = models.CharField(max_length=200,unique=True,verbose_name=u'Name of discipline')
    course = models.ForeignKey(Course)
    chair = models.ForeignKey(Chair)
    def __unicode__(self):
        return self.name

class Group(models.Model):
    name = models.CharField(max_length=200,unique=True,verbose_name=u'Name of group')
    course = models.ForeignKey(Course)
    def __unicode__(self):
        return self.name
