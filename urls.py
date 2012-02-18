from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'LongwittonServer.views.home', name='home'),
    # url(r'^LongwittonServer/', include('LongwittonServer.foo.urls')),
    url(r'^current/$', 'longwitton.views.current'),

    url(r'^update/(?P<new_url>.+)$', 'longwitton.views.update'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
