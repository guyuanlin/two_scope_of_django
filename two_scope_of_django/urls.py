from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from rest_framework import routers
from flavors import views as flavors_views
router = routers.DefaultRouter()
router.register(r'flavors', flavors_views.FlavorViewSet)

urlpatterns = patterns(
	'',
	url(r'^', include(router.urls)),
	url(r'^admin/', include(admin.site.urls)),
	url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
	url(r'^flavor/', include('flavors.urls')),
)
