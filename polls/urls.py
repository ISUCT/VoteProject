from django.conf.urls.defaults import patterns, include, url
from django.views.generic import DetailView, ListView
from models import Poll
import views
urlpatterns = patterns('',
	#url(r'^polls/', 'polls.views.polls'),
    url(r'^(?P<poll_id>\d+)/$', views.detail, name='detail'),
    url(r'^(?P<poll_id>\d+)/vote/$', views.vote, name='vote'),
    url(r'^polls/', include('polls.urls', namespace="polls")),
    url(r'^(?P<poll_id>\d+)/results/$', views.results, name='results'),
	url(r'^index/', views.index, name='index'),
	#url(r'^test/', 'polls.views.test'),
)

