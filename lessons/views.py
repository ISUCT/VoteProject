from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import Context, loader
from django.shortcuts import render, get_object_or_404, render_to_response
from django.template.context import RequestContext
from django.core.urlresolvers import reverse
from lessons.forms import LessonForm
from models import Lesson

def addLesson(request):
    user = request.user
    if user.is_authenticated():
        lessonForm = LessonForm(request.POST)
        if request.method == 'POST':
            print(lessonForm)
            lesson = Lesson()
            if lessonForm.is_valid():
                print(lessonForm)
                lesson.group = lessonForm.cleaned_data['group']
                lesson.discipline = lessonForm.cleaned_data['discipline']
                lesson.dateAndTtime = lessonForm.cleaned_data['dateAndTtime']
                lesson.room = lessonForm.cleaned_data['room']
                lesson.lessonID = lessonForm.cleaned_data['lessonID']
                lesson.status = lessonForm.cleaned_data['status']
                lesson.user = lessonForm.cleaned_data['user']
                lesson.save()
                return HttpResponseRedirect('/admin')
        return render_to_response('dokladedit.html', {'form': lessonForm}, context_instance=RequestContext(request))
    #text = """<html><body><h1>Hello world</h1><p>asdfgvbasdbg</p></body></html>"""
    #text2 = "hello again"
    #return HttpResponse(text)
    return render(request,'vote/create.html', {})



