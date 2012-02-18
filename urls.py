from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'LongwittonServer.views.home', name='home'),
    # url(r'^LongwittonServer/', include('LongwittonServer.foo.urls')),

    # Backwards-compatibility alias
    url(r'^current/$', 'longwitton.views.chasee_current'),

    url(r'^chasee/current/$', 'longwitton.views.chasee_current'),
    url(r'^chasee/target/$', 'longwitton.views.chasee_target'),
    url(r'^chasee/update/(?P<new_url>.+)$', 'longwitton.views.chasee_update'),

    url(r'^chaser/update/(?P<new_url>.+)$', 'longwitton.views.chaser_update'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
