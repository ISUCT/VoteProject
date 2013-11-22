# -*- coding=utf8 -*-
#from django.conf.urls import patterns, include, url
from django.conf.urls import patterns, include, url
import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()
from django.views.generic import DetailView, ListView
from polls.models import Poll

urlpatterns = patterns('',
    # Examples:
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:

    #url(r'^test/', 'testForms.views.contact'),
    #url(r'^accounts/', include('accounts.urls')),
    # Подключаем урлы приложения конференция
    #url(r'^accounts/', include('conference.urls')),
    #url(r'^', include('conference.urls')),
    #url(r'^', include('accounts.urls')),
    url(r'^', include('polls.urls')),
    url(r'^', include('lessons.urls')),
    url(r'^', include('department.urls')),
    url(r'^admin/', include(admin.site.urls)),
    #url(r'^accounts/', include('registration.urls')),
    #url(r'^$', 'BaseProject.views.home'),  # Основная страница с информацией
    #url(r'^news/$', 'BaseProject.views.news'),  # Новости
    #url(r'^contact/$', 'BaseProject.views.contacts'),  # Контакты
    #url(r'^schedule/$', 'BaseProject.views.schedule'),
    #url(r'^agreement/$', 'BaseProject.views.agreement'),
    #чтобы правильно отображать статику на сервере
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
)
if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += staticfiles_urlpatterns()
