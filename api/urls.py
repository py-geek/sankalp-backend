from django.conf.urls import patterns, include, url
from django.contrib import admin


from api import views

admin.autodiscover()


urlpatterns = patterns('',
    url(r'^events/',views.EventList.as_view()),
)
