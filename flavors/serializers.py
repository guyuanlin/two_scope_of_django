from rest_framework import serializers

from . import models


class FlavorSerializer(serializers.ModelSerializer):

	class Meta:
		model = models.Flavor
		fields = ('title', 'slug', 'scoops_remaining')