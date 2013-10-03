# -*- coding=utf8 -*-
from django.shortcuts import render_to_response, redirect
from django.template.context import RequestContext
from django.http import HttpResponseRedirect
from department.forms import FacultyForm
#from models import Section, Doklad
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def FacultyAdd(request):
    #создаем экземпляр отображаемой формы (forms.py)
    facultyForm = FacultyForm(request.POST)
    #Возвращаем пользователю страничку в ответ на запрос (шаблон, form подменяем на созданную выше форму, остальное просто надо)
    return render_to_response('dokladedit.html', { 'form': facultyForm}, context_instance=RequestContext(request))

