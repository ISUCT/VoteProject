#-*- coding=utf8 -*-
'''
Created on 16.06.2012

@author: jskonst
'''
import glob
from django.shortcuts import render_to_response
#from django.http import HttpResponse
from django.template.context import RequestContext
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import settings


def home(request):
    text = "hello world"
    return render_to_response('test.html', {'content': text}, RequestContext(request))
