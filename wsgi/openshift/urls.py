from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'openshift.views.home', name='home'),
    # url(r'^openshift/', include('openshift.foo.urls')),

    url(r'^admin/', include(admin.site.urls)),

    ### UNCOMENT BELOW TO ACTIVATE CELERY
    #url(r'celery/(?P<taskname>.*)/', 'openshift.views.task')
    
    # As per https://docs.djangoproject.com/en/1.7/howto/static-files/#serving-files-uploaded-by-a-user-during-development
    # you should be using a dedicated server or CDN.
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
