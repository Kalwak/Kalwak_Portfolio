from django.test import TestCase, override_settings
from rest_framework.test import APIClient
from rest_framework import status
from Project.models import Project


class LogsTestCase(TestCase):

    def setUp(self) -> None:
        self.client = APIClient()

    def test_404(self):
        path = '/api/project/2'
        self.client.get()
