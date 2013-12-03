# -*- coding=utf8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _

# Необходимо сделать сортировку объектов каждого класса (Например, дисциплины по алфавиту)
class Faculty(models.Model):
    name = models.CharField(max_length=200,unique=True,verbose_name=u'Имя факультета') 
    def __unicode__(self):
        return self.name
    class Meta(object):
        verbose_name_plural = "Факультеты"
        verbose_name = "факультет"

class Chair(models.Model): 
    name = models.CharField(max_length=200,unique=True,verbose_name=u'Имя кафедры') 
    faculty = models.ForeignKey(Faculty, verbose_name = "Факультет") 
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
    course = models.ForeignKey(Course, verbose_name = "Курс")
    chair = models.ForeignKey(Chair, verbose_name = "Кафедра")
    def __unicode__(self):
        return self.name
    class Meta(object):
        verbose_name_plural = "Дисциплины"
        verbose_name = "дисциплину"

class Group(models.Model): # Создаем класс "Группа"
    name = models.CharField(max_length=200,unique=True,verbose_name=u'Номер группы') # Добавляем поле "Номер группы" в переменную name. Здесь же задаем максимальную длину поля, уникальность и название, которое будет выводиться в админке
    course = models.ForeignKey(Course, verbose_name = "Курс") # с помощью метода ForeignKey делаем ссылку на объект Course, в verbose_name задаем, как будет выводиться в админке
    def __unicode__(self):
        return self.name # В этом методе возвращаем текущий объект, чтобы он мог выводиться в админке
    class Meta(object):
        verbose_name_plural = "Группы" # Задаем имя, которое будет выводиться в админке. Имя по умолчанию - название класса. Это то, что будет выводиться в основном меню
        verbose_name = "группу" # А такое имя увидим при редактировании





