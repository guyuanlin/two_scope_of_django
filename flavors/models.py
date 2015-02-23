from django.db import models


class Flavor(models.Model):

	title = models.CharField(
		max_length=30
	)
	slug = models.CharField(
		max_length=30,
		unique=True
	)
	scoops_remaining = models.IntegerField(
		default=0
	)