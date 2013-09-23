from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import Context, loader
from django.shortcuts import render, get_object_or_404, render_to_response
from django.template.context import RequestContext
from django.core.urlresolvers import reverse


def addLesson(request):
    #text = """<html><body><h1>Hello world</h1><p>asdfgvbasdbg</p></body></html>"""
    #text2 = "hello again"
    #return HttpResponse(text)
    return render(request,'vote/create.html', {})



