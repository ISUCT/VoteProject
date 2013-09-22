# -*- coding=utf8 -*-
from django.contrib import admin
from department.models import Lesson

class LessonAdmin(admin.ModelAdmin):
    model = Lesson
    list_display = ('status', 'disciplie', 'group', 'user') 
    display_name = "jkfgnjdfkgn"

admin.site.register(Lesson, LessonAdmin)
