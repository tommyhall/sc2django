from django.conf.urls import patterns, url
from sc2stats import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^/about/$', views.about, name='about'),
    url(r'^/playerstats/$', views.playerstats, name='playerstats'),
    url(r'^/balancereport/$', views.balancereport, name='balancereport')
)
