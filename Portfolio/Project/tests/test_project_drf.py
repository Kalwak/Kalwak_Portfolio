from django.test import TestCase, override_settings
from django.utils import timezone
from rest_framework.test import APIClient
from rest_framework import status
from rest_framework.utils import json

from Project.models import Project


class ProjectTestCase(TestCase):

    def setUp(self) -> None:
        self.client = APIClient()

    def test_404(self):
        path = '/api/project/100/'
        response = self.client.get(path)
        expected = status.HTTP_404_NOT_FOUND
        self.assertEqual(response.status_code, expected)

    def test_405(self):
        data = {
            'name': 'test',
            'cover_page': 'cover_pages/photo.jpg',
            'description': 'ok',
            'website': 'http://kalwak.xyz',
            'date': timezone.now()
        }
        path = '/api/project/'
        response = self.client.post(path, data)
        expected = status.HTTP_405_METHOD_NOT_ALLOWED
        self.assertEqual(response.status_code, expected)

    def test_200(self):
        Project.objects.create(
            name="Test",
            cover_page="cover_page/image.jpg",
            description="ok",
            website="http://kalwak.xyz",
            date=timezone.now()
        )
        path = '/api/project/1/'
        response = self.client.get(path)
        expected = status.HTTP_200_OK
        self.assertEqual(response.status_code, expected)

    def test_200_content(self):
        Project.objects.create(
            name="Test",
            cover_page="cover_page/image.jpg",
            description="ok",
            website="http://kalwak.xyz",
            date=timezone.now()
        )
        path = '/api/project/2/'
        response = self.client.get(path)
        expected = status.HTTP_200_OK
        self.assertEqual(response.status_code, expected)
        data = json.loads(response.content)["website"]
        expected = "http://kalwak.xyz"
        self.assertEqual(data, expected)
