from django.conf.urls import include, url
from views.status import Status as ServiceStatus
from views.initialization import InitSystem
from views.assets import AssetList, AssetFetch, AssetUpdate, AssetDelete, AssetCreate
from views.type import TypeList, NestedTypeList
from views.category import CategoryList
from views.media import ImageUpload, VoiceUpload

urlpatterns = [
	url(r'^status/$', ServiceStatus.as_view()),
	url(r'^init/$', InitSystem.as_view()),

	# Asset Management
	url(r'^asset/list/$', AssetList.as_view(), name="asset-list"),
	url(r'^asset/(?P<asset_id>[0-9A-Fa-f]*)/$', AssetFetch.as_view(), name="asset-list"),
	url(r'^asset/update/(?P<asset_id>[0-9A-Fa-f]*)/$', AssetFetch.as_view(), name="asset-update"),
	url(r'^asset/delete/(?P<asset_id>[0-9A-Fa-f]*)/$', AssetDelete.as_view(), name="asset-delete"),
	url(r'^asset/create/$', AssetCreate.as_view(), name="asset-create"),

	# Asset-Category Management
	url(r'^asset/category/list/$', CategoryList.as_view(), name="categ-list"),
	# url(r'^asset/category/delete/(?P<categ_id>[0-9A-Fa-f]*)/$', ServiceStatus.as_view(), name="categ-delete"),	
	# url(r'^asset/category/update/(?P<categ_id>[0-9A-Fa-f]*)/$', ServiceStatus.as_view(), name="categ-update"),	

	# Asset-Type Management
	url(r'^asset/type/list/$', TypeList.as_view(), name="type-list"),
	url(r'^asset/type/list/(?P<category_id>[0-9A-Fa-f]*)/$', NestedTypeList.as_view(), name="type-list-nested"),

	# Asset Media Management
	url(r'^asset/media/image-upload/(?P<asset_id>[0-9A-Fa-f]*)/$', ImageUpload.as_view(), name="media-image-upload"),
	url(r'^asset/media/voice-upload/(?P<asset_id>[0-9A-Fa-f]*)/$', VoiceUpload.as_view(), name="media-voice-upload"),
]