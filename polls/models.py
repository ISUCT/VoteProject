# -*- coding=utf8 -*-
from django.db import models
from django.utils import timezone
import datetime

class Poll(models.Model):
    question = models.CharField(max_length=200)
    pub_date = models.DateTimeField('Дата опроса')
    def __unicode__(self):
        return self.question
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'
    class Meta(object):
        verbose_name_plural = "Опрос"
        verbose_name = "опроса"

# Как переименовать поле Question?

class Choice(models.Model):
    poll = models.ForeignKey(Poll)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __unicode__(self):
        return self.choice_text
    class Meta(object):
        verbose_name_plural = "Варианты ответа"
        verbose_name = "вариант"

