from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'openshift.views.home', name='home'),
    # url(r'^openshift/', include('openshift.foo.urls')),

    url(r'^admin/', include(admin.site.urls)),

    ### UNCOMENT BELOW TO ACTIVATE CELERY
    #url(r'celery/(?P<taskname>.*)/', 'openshift.views.task')
)
