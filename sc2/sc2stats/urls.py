from django.conf.urls import patterns, url
from sc2stats import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^/about/$', views.about, name='about'),
    url(r'^/win_rate_report/$', views.win_rate_report, name='win_rate_report')
)
