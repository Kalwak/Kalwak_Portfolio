from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status

from Portfolio import settings
from Portfolio.settings import BASE_DIR
from Service.models import File, ServiceRequest
import os


class ServiceTestCase(TestCase):

    def setUp(self) -> None:
        self.client = APIClient()
        self.file_path = os.path.join(BASE_DIR,
                                      'Service/tests/files/test_file.txt')
        self.file_pdf_path = os.path.join(BASE_DIR,
                                          'Service/tests/files/test.pdf')

    def test_service_get(self):
        response = self.client.get("/api/service_request/")
        status_expected = status.HTTP_405_METHOD_NOT_ALLOWED
        self.assertEqual(response.status_code, status_expected)

    # TODO needs to be remade because of the changes
    """
    def test_service_request_post_successful(self):
        data = {"name": "Fooname",
                "email": "fooo@gmail.com",
                "description": "foodescription",
                "telephone": "84599021"}
        response = self.client.post('/api/service_request/', data=data,
                                    format='json')
        self.assertEqual(response.status_code, status.HTTP_302_FOUND)
        response.data.pop("files")
        response.data.pop("services")
        self.assertEqual(response.data, data)"""

    def test_service_request_wrong_email(self):
        data = {"name": "Fooname",
                "email": "fooo",
                "description": "foodescription",
                "telephone": "84599021"}
        response = self.client.post('/api/service_request/', data=data,
                                    format='json')
        self.assertEqual(response.status_code, status.HTTP_302_FOUND)
        correct_response = f"{settings.FRONTEND_URL}/hire-us/?errors=%7B\'email\':%20[\'Enter%20a%20valid%20email%20address.\']%7D"
        self.assertEqual(response.url, correct_response)

    def test_service_request_name_emply(self):
        data = {"name": "",
                "email": "fooo@gmail.com",
                "description": "foodescription",
                "telephone": "84599021"}
        response = self.client.post('/api/service_request/', data=data,
                                    format='json')
        self.assertEqual(response.status_code, status.HTTP_302_FOUND)
        correct_response = f"{settings.FRONTEND_URL}/hire-us/?errors=%7B\'name\':%20[\'This%20field%20may%20not%20be%20blank.\']%7D"
        self.assertEqual(response.url, correct_response)

    def test_service_request_description_emply(self):
        data = {"name": "Fooname",
                "email": "fooo@gmail.com",
                "description": "",
                "telephone": "84599021"}
        response = self.client.post('/api/service_request/', data=data,
                                    format='json')
        self.assertEqual(response.status_code, status.HTTP_302_FOUND)
        correct_response = f"{settings.FRONTEND_URL}/hire-us/?errors=%7B\'description\':%20[\'This%20field%20may%20not%20be%20blank.\']%7D"
        self.assertEqual(response.url, correct_response)

    def test_service_request_missing_email_field(self):
        data = {"name": "FooName",
                "description": "foodescription",
                "telephone": "84599023"}
        response = self.client.post('/api/service_request/', data=data,
                                    format='json')
        self.assertEqual(response.status_code, status.HTTP_302_FOUND)
        correct_response = f"{settings.FRONTEND_URL}/hire-us/?errors=%7B\'email\':%20[\'This%20field%20is%20required.\']%7D"
        self.assertEqual(response.url, correct_response)

    def test_service_request_missing_name_field(self):
        data = {"email": "fooo@gmail.com",
                "description": "foodescription",
                "telephone": "84599023"}
        response = self.client.post('/api/service_request/', data=data,
                                    format='json')
        self.assertEqual(response.status_code, status.HTTP_302_FOUND)
        correct_response = f"{settings.FRONTEND_URL}/hire-us/?errors=%7B\'name\':%20[\'This%20field%20is%20required.\']%7D"
        self.assertEqual(response.url, correct_response)

    def test_service_request_missing_description_field(self):
        data = {"name": "Fooname",
                "email": "fooo@gmail.com",
                "telephone": "84599021"}
        response = self.client.post('/api/service_request/', data=data,
                                    format='json')
        self.assertEqual(response.status_code, status.HTTP_302_FOUND)
        correct_response = f"{settings.FRONTEND_URL}/hire-us/?errors=%7B\'description\':%20[\'This%20field%20is%20required.\']%7D"
        self.assertEqual(response.url, correct_response)

    # TODO needs to be remade because of the changes
    """def test_service_request_saving_file(self):
        data = {"name": "Fooname",
                "email": "fooo@gmail.com",
                "description": "foodescription",
                "telephone": "84599021",
                "file": open(self.file_path, 'rb')}
        response = self.client.post('/api/service_request/', data=data,
                                    format='multipart')
        data.pop('file')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        response.data.pop("files")
        response.data.pop("services")
        self.assertEqual(response.data, data)
        saved_file = File.objects.last()
        self.assertEqual(saved_file.service.email, "fooo@gmail.com")
        saved_file.service.delete()
        saved_file.delete()"""

    # TODO needs to be remade because of the changes
    """def test_service_request_saving_several_files(self):
        data = {"name": "Fooname",
                "email": "fooo@gmail.com",
                "description": "foodescription",
                "telephone": "84599021",
                "file1": open(self.file_path, 'rb'),
                "file2": open(self.file_pdf_path, 'rb')}
        response = self.client.post('/api/service_request/', data=data,
                                    format='multipart')
        data.pop('file1')
        data.pop('file2')
        self.assertEqual(response.status_code, status.HTTP_302_FOUND)
        response.data.pop("files")
        response.data.pop("services")
        self.assertEqual(response.data, data)
        saved_file = File.objects.last()
        self.assertEqual(saved_file.service.email, "fooo@gmail.com")
        saved_file.delete()
        saved_file = File.objects.last()
        self.assertEqual(saved_file.service.email, "fooo@gmail.com")
        saved_file.service.delete()
        saved_file.delete()"""
