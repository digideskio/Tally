from django.conf.urls import *


urlpatterns = patterns('testtool.main.views',
    # Subject URLs
    url(r'^$',                                  'index',  name='home'),
    url(r'^(?P<test_instance_id>\d+)/tally/$',  'tally',  name='tally'),
    url(r'^(?P<test_instance_id>\d+)/status/$', 'status', name='status'),
    
    # Desktop App URLs
    url(r'^(?P<test_instance_id>\d+)/init/$',      'init_test_instance', name='init_test_instance'),
    url(r'^(?P<test_instance_id>\d+)/get_media/$', 'get_media',          name='get_media'),
)
