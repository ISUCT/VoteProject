# -*- coding=utf8 -*-
from django.conf.urls.defaults import patterns, url
from registration.views import RegistrationView
from forms import UserRegistrationForm
from views import profile, userlist, userbage

#Урлы для настройки профиля пользователя
urlpatterns = patterns('',
    url(r'^userlist/$', userlist),
    url(r'^userbage/$', userbage),
    url(r'^profile/$', profile),
    url(r'^register/$', RegistrationView, {'backend': 'accounts.backend.RegBackend', 'form_class': UserRegistrationForm}, name='registration_register'),
    )
