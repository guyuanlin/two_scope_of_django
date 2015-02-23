import json
from django.core.urlresolvers import reverse
from django.test import TestCase
from django.utils.http import urlencode

from flavors.models import Flavor

class FlavorAPITests(TestCase):

	def setUp(self):
		Flavor.objects.get_or_create(title="A Title", slug="a-slug")
	
	def test_list(self):
		url = reverse("flavor_object_api")
		response = self.client.get(url)
		self.assertEquals(response.status_code, 200)
		data = json.loads(response.content)$


class DjangoRestFrameworkTests(TestCase):

	def setUp(self):
		Flavor.objects.get_or_create(title="title1", slug="slug1")
		Flavor.objects.get_or_create(title="title2", slug="slug2")
		self.create_read_url = reverse("flavor-list")
		self.read_update_delete_url = \
			reverse("flavor-detail", kwargs={"slug": "slug1"})

	def test_list(self):
		response = self.client.get(self.create_read_url)
		# Are both titles in the content?
		self.assertContains(response, "title1")
		self.assertContains(response, "title2")

	def test_detail(self):
		response = self.client.get(self.read_update_delete_url)
		data = json.loads(response.content)
		content = {
			u'title': u'title1',
			u'slug': u'slug1',
			u'scoops_remaining': 0
		}
		self.assertEquals(data, content)

	def test_create(self):
		post = {"title": "title3", "slug": "slug3"}
		response = self.client.post(self.create_read_url, post)
		data = json.loads(response.content)
		self.assertEquals(response.status_code, 201)
		content = {
			u'title': u'title3',
			u'slug': u'slug3',
			u'scoops_remaining': 0
		}
		self.assertEquals(data, content)
		self.assertEquals(Flavor.objects.count(), 3)
		
	def test_delete(self):
		response = self.client.delete(self.read_update_delete_url)
		self.assertEquals(response.status_code, 204)
		self.assertEquals(Flavor.objects.count(), 1)

	def test_update(self):
		# urlencode the PUT because self.client.put doesn't do it.
		put = urlencode({
			"title": "Triple Peanut Butter Cup",
			"slug": "triple-peanut-butter-cup"
		})
		# This only applies to Django 1.5+
		# Send as form data or Django"s client.put uses
		#   "application/octet-stream".
		response = self.client.put(
			self.read_update_delete_url,
			put,
			content_type="application/x-www-form-urlencoded"
		)
		self.assertEquals(response.status_code, 200)
		self.assertEquals(
			Flavor.objects.get(pk=1).title,
			"Triple Peanut Butter Cup"
		)