# -*- coding=utf8 -*-
from django.conf.urls import patterns, url
#from registration.views import RegistrationView
#from forms import UserRegistrationForm
from views import FacultyAdd

urlpatterns = patterns('',
    url(r'^faculty_add/$', FacultyAdd),
    #url(r'^userbage/$', userbage),
    #url(r'^profile/$', profile),
    #url(r'^register/$', RegistrationView, {'backend': 'accounts.backend.RegBackend', 'form_class': UserRegistrationForm}, name='registration_register'),
    )
