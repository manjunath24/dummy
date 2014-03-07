from django.conf.urls import patterns, include, url

from .views import InstituteCreateView


urlpatterns = patterns('',
                       url(r'^registration/$',
                           InstituteCreateView.as_view(),
                           name='institute_registration'),)
