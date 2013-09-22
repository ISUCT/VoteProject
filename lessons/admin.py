# -*- coding=utf8 -*-
from django.contrib import admin
from lessons.models import Lesson

class LessonAdmin(admin.ModelAdmin):
    model = Lesson
    list_display = ('status', 'discipline', 'group', 'user') 

admin.site.register(Lesson, LessonAdmin)
