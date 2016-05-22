from django.conf.urls import url

from . import views

app_name = 'polls'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^AddTask/$', views.AddTask, name='AddTask'),
    url(r'^ListOnDueDate/$', views.ListOnDueDate, name='ListOnDueDate'),
    url(r'^CrossedDates/$', views.CrossedDates, name='CrossedDates'),
    url(r'^ListOnDay/$', views.ListOnDay, name='ListOnDay'),
    url(r'^ListOnWeek/$', views.ListOnWeek, name='ListOnWeek'),
    url(r'^ListOnYear/$', views.ListOnYear, name='ListOnYear'),
    url(r'^ListOnMonth/$', views.ListOnMonth, name='ListOnMonth'),
    url(r'^EditStatus/(?P<pk>\d+)/$', views.EditStatus, name='EditStatus'),
    url(r'^(?P<id>[0-9]+)/$', views.TaskInfo, name='TaskInfo')
    
]