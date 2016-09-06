from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.conf import settings

from . import sitemaps, robots

sitemaps = {
    'views': sitemaps.ViewSitemap([
        ('website:index', '1.0', 'monthly'),
        ('website:projects', '0.85', 'monthly'),
        ('blog:main', '0.85', 'monthly'),
        ('website:contact', '0.85', 'monthly'),
    ]),
}

urlpatterns = [
    url(r'^', include('website.urls', namespace="website")),
    url(r'^api/', include('api.urls', namespace="api")),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^_ah/', include('djangae.urls')),
]

# if settings.DEBUG:
#     urlpatterns.append(url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}))
