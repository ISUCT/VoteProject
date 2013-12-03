# -*- coding=utf8 -*-
from models import Lesson
from django import forms

class LessonForm(forms.ModelForm):

    class Meta:
        model = Lesson
        #fields = {'section', }#Добавляем поля, которые будут отображаться
        exclude = ('user', 'lessonID')# Список полей, которые исключаем из формы
