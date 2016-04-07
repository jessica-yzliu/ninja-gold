from django.conf.urls import patterns, url
from . import views

urlpatterns = patterns('',
    url(r'^$', views.index, name="index"),
    url(r'^ninja-gold$', views.find_gold, name="ninja-gold"),
)
