# -*- coding=utf8 -*-
from django.shortcuts import render_to_response, redirect
from django.template.context import RequestContext
from django.http import HttpResponseRedirect
from department.forms import FacultyForm
from models import Faculty
#from models import Section, Doklad
#from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def FacultyAdd(request):
    user = request.user
    if user.is_authenticated():
        facultyForm = FacultyForm(request.POST)
        # Проверяем - если браузер присылает данные (запрос) по методу Post
        if request.method == 'POST':
            # Создем экземпляр модели данных факультета (новый факультет)
            faculty = Faculty()
            #создаем экземпляр отображаемой формы (forms.py)
            #Возвращаем пользователю страничку в ответ на запрос (шаблон, form подменяем на созданную выше форму, остальное просто надо)
            if facultyForm.is_valid():
                # Заполним содержимое факультета и сохраним его
                faculty.name = facultyForm.cleaned_data['name']
                faculty.save()
                #lesson.lessonID=date+room
                #lesson.user = user
                return HttpResponseRedirect('/admin')
        return render_to_response('dokladedit.html', { 'form': facultyForm}, context_instance=RequestContext(request))
    return HttpResponseRedirect('/admin')

    #user = request.user
    #if user.is_authenticated():
        #profile = user.get_profile()
        ## необходимо проверить - а установлено ли у него то, что он докладчик
        #if profile.dokladchik:
            #if request.method == 'POST':

# Вот это надо посмотреть, случай если пользователь уже вводил данные в форму
#######################################################################################################
                #if 'form_data' in request.session:
                    #doklad = request.session['form_data']
                    #dokladForm = DokladForm(request.POST, instance=doklad)
                #else:
                    #doklad = Doklad()
                    #dokladForm = DokladForm(request.POST)
#######################################################################################################

                #if dokladForm.is_valid():
                    ## Создадим новый доклад и сохраним его
                    #doklad.section = dokladForm.cleaned_data['section']
                    #doklad.title = dokladForm.cleaned_data['title']
                    #doklad.authors = dokladForm.cleaned_data['authors']
                    #doklad.text = dokladForm.cleaned_data['text']
                    #doklad.publish = dokladForm.cleaned_data['publish']
                    #doklad.save()
                    #doklad.author.add(profile)
                    #return HttpResponseRedirect('/accounts/profile/dokladlist')

            #else:
                #if 'form_data' in request.session:
                    #dokladForm = DokladForm(instance=request.session['form_data'])
                #else:
                    #dokladForm = DokladForm()

            #return render_to_response('dokladedit.html', {'title': "Редактировать доклад", 'form': dokladForm}, context_instance=RequestContext(request))

        #else:
            ## Редиректим на профиль
            #return HttpResponseRedirect('/accounts/profile/')
    #else:
        ## Перенаправляем на страницу входа
        #return HttpResponseRedirect('/accounts/login/')
