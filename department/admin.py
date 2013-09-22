# -*- coding=utf8 -*-
from django.contrib import admin
from department.models import Faculty, Chair, Course, Discipline, Group

class FacultyAdmin(admin.ModelAdmin):
    model = Faculty
    #list_display = ('name', )

class ChairAdmin(admin.ModelAdmin):
    model = Chair

class CourseAdmin(admin.ModelAdmin):
    model = Course

class DisciplineAdmin(admin.ModelAdmin):
    model = Discipline
    list_display = ('name','course') 

class GroupAdmin(admin.ModelAdmin):
    model = Group

# А вот теперь регистрируем их
admin.site.register(Faculty, FacultyAdmin)
admin.site.register(Chair, ChairAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Discipline, DisciplineAdmin)
admin.site.register(Group, GroupAdmin)

