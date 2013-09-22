# -*- coding: utf-8 -*-
from django.conf.urls.defaults import patterns, include, url
from django.views.generic import DetailView, ListView
urlpatterns = patterns('',
	url(r'^add_lesson/', 'lessons.views.addLesson'),	
)

