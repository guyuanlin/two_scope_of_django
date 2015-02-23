import json
from rest_framework import viewsets
from django.http import HttpResponse

from . import models, serializers

def objects(request):

	flavors = list(models.Flavor.objects.values())
	return HttpResponse(
		json.dumps(flavors),
		content_type='application/json'
	)


class FlavorViewSet(viewsets.ModelViewSet):

	queryset = models.Flavor.objects.all()
	serializer_class = serializers.FlavorSerializer
	lookup_field = 'slug'