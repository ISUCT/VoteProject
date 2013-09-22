from django.conf.urls.defaults import patterns, include, url
from django.views.generic import DetailView, ListView
from models import Poll
urlpatterns = patterns('',
	#url(r'^polls/', 'polls.views.polls'),
        #url(r'^polls/', include('polls.urls', namespace="polls")),
	url(r'^test/', 'polls.views.test'),	
)

