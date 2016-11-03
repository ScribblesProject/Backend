from django.conf.urls import include, url
from views.home import Home

urlpatterns = [
    url(r'^$', Home.as_view(), name='index'),
    url(r'^auth/(?P<asset_id>[0-9A-Fa-f]*)/$', AssetFetch.as_view(), name="asset-list")

]
