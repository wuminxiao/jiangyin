from django.conf.urls.defaults import *

urlpatterns = patterns('',
        (r'^access_verify','chihuo.core.views.access_verify'),
        )
