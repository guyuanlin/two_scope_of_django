from django.conf.urls import patterns, url

from . import views


urlpatterns = patterns(
	'',
	url(r'^objects/$', views.objects, name='flavor_object_api'),
)