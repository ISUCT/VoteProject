# -*- coding=utf8 -*-
from models import Lesson
from django import forms
#from datetimewidget.widgets import DateTimeWidget

class LessonForm(forms.ModelForm):
    #mydate = forms.DateField(widget=CalendarWidget)
    #mytime = forms.TimeField(widget=widgets.AdminTimeWidget)
    #mydatetime = forms.DateTimeField(widget=DateTimeWidget)

    class Meta:
        model = Lesson
        #fields = {'section', }#Добавляем поля, которые будут отображаться
        exclude = ('user', 'lessonID')# Список полей, которые исключаем из формы
         #widgets = {
            ##Use localization
            #'datetime': DateTimeWidget(attrs={'id':"yourdatetimeid"}, usel10n = True)
        #}


