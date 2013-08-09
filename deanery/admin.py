# -*- coding=utf8 -*-
from django.contrib import admin
from deanery.models import Faculty, Chair

class FacultyAdmin(admin.ModelAdmin):
    model = Faculty
    #list_display = ('name', )

class ChairAdmin(admin.ModelAdmin):
    model = Chair
# тут их регистрация
admin.site.register(Faculty, FacultyAdmin)
admin.site.register(Chair, ChairAdmin) 
