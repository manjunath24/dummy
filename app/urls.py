from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
                       url(r'^registration/$', 'app.views.sign_up',
                           name='institute_registration'),
                       url(r'^confirm/$', 'app.views.confirm', name='confirm_signup'),)
