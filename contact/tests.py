from rest_framework import status
from rest_framework.test import APITestCase

from django.contrib.auth import get_user_model
from rest_framework.utils import json

from .models import Contact
from rest_framework.reverse import reverse
# from contact import views

User = get_user_model()


class PlivoContactsTests(APITestCase):
    def test_post_count(self):
        Contact.objects.create(name="TEST1", email="test@test.com", mobile=000000000)
        count = Contact.objects.count()
        self.assertEquals(count, 1)

    def test_get_count(self):
        data = {}
        url = reverse('contacts')
        response = self.client.get(url, data, format='json')
        self.assertEquals(response.status_code, status.HTTP_200_OK)

    def test_search_filter_name(self):
        data = {}
        url = reverse('contacts')
        response = self.client.get(url+"?name=TEST1", data, format='json')
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        body_unicode = response.body.decode('utf-8')
        body = json.loads(body_unicode)
        count = int(body['count'])
        self.assertEquals(count, 1)

    def test_search_filter_email(self):
        data = {}
        url = reverse('contacts')
        response = self.client.get(url+"?email=test@test.com", data, format='json')
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        body_unicode = response.body.decode('utf-8')
        body = json.loads(body_unicode)
        count = int(body['count'])
        self.assertEquals(count, 1)
