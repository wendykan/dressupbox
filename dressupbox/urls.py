from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^app/$', 'app.views.default'),
    url(r'^login/$', 'app.views.login'),
    url(r'^signup/$', 'app.views.signup'),
    url(r'^map/$', 'app.views.map'),
    url(r'^dress/(?P<dress_id>\d+)/$', 'app.views.dress'),
    url(r'^moreinfo/$', 'app.views.moreinfo'),
    url(r'^search/$', 'app.views.search'),
    url(r'^results/$', 'app.views.results'),
    # url(r'^app/(?P<poll_id>\d+)/$', 'app.views.detail'),
    # url(r'^app/(?P<poll_id>\d+)/results/$', 'app.views.results'),
    # url(r'^app/(?P<poll_id>\d+)/vote/$', 'app.views.vote'),
    url(r'^admin/', include(admin.site.urls)),
    
)

if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += patterns('',
        (r'^imgs/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT}))

