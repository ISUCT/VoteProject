# -*- coding=utf8 -*-
from django.conf.urls.defaults import patterns, url
from accounts import views
#from registration.views import RegistrationView
#from forms import UserRegistrationForm
#from views import profile, userlist, userbage

#Урлы для настройки профиля пользователя
urlpatterns = patterns('',
    url(r'^logout/$', 'django.contrib.auth.views.logout',{'template_name':'registration/logout.html'}, name='logout'),
    url(r'^login/$', 'django.contrib.auth.views.login', name='login'),
    url(r'^profile/$', views.uProfile, name='profile'),
    #url(r'^userbage/$', userbage),
    #url(r'^profile/$', profile),
    #url(r'^register/$', RegistrationView, {'backend': 'accounts.backend.RegBackend', 'form_class': UserRegistrationForm}, name='registration_register'),
    )
