from django.conf.urls import patterns, url,include
#not sure if I still need to import polls
from polls import views

#ex: /polls/
urlpatterns = patterns('',
url(r'^$', views.index, name ='index'),
url(r'^(?P<poll_id>\d+)/$',views.detail, name = 'detail'),
url(r'^(?P<poll_id>\d+)/results/$',views.results, name = 'results'),
url(r'^(?P<poll_id>\d+)/vote/$',views.vote, name = 'vote'),


)



