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
            lesson = Lesson()
            if lessonForm.is_valid():
                lesson.name = lessonForm.cleaned_data['group', 'discipline', 'dateAndTtime', 'room', 'lessonID', 'status', 'user']
                lesson.save()
                return HttpResponseRedirect('/admin')
        return render_to_response('dokladedit.html', { 'form': lessonForm}, context_instance=RequestContext(request))
    #text = """<html><body><h1>Hello world</h1><p>asdfgvbasdbg</p></body></html>"""
    #text2 = "hello again"
    #return HttpResponse(text)
    return render(request,'vote/create.html', {})



