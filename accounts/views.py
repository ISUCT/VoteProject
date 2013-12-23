# coding: utf8
# Create your views here.
#import glob
from django.shortcuts import render_to_response, render
#from django.http import HttpResponse
from django.template.context import RequestContext


def logout(request):
    text = "leave so soon?"
    #return render_to_response('test.html', {'content': text}, RequestContext(request))
    return render(request,'test.html', {'content': text})

def login(request):
    text = "whant to come in?"
    return render_to_response('test.html', {'content': text}, RequestContext(request))
