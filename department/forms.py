# -*- coding=utf8 -*-
from models import Faculty
from django import forms

class FacultyForm(forms.ModelForm):

    class Meta:
        model = Faculty
        #fields = {'section', }#Добавляем поля, которые будут отображаться
        #exclude = ('author')# Список полей, которые исключаем из формы


