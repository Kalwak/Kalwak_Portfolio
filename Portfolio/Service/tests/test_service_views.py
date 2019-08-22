from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
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

    def test_service_request_post_successful(self):
        data = {"name": "Fooname",
                "email": "fooo@gmail.com",
                "description": "foodescription"}
        response = self.client.post('/api/service_request/', data=data,
                                    format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data, data)

    def test_service_request_wrong_email(self):
        data = {"name": "Fooname",
                "email": "fooo",
                "description": "foodescription"}
        response = self.client.post('/api/service_request/', data=data,
                                    format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        correct_response = b'{"email":["Enter a valid email address."]}'
        self.assertEqual(response.content, correct_response)

    def test_service_request_name_emply(self):
        data = {"name": "",
                "email": "fooo@gmail.com",
                "description": "foodescription"}
        response = self.client.post('/api/service_request/', data=data,
                                    format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        correct_response = b'{"name":["This field may not be blank."]}'
        self.assertEqual(response.content, correct_response)

    def test_service_request_description_emply(self):
        data = {"name": "Fooname",
                "email": "fooo@gmail.com",
                "description": ""}
        response = self.client.post('/api/service_request/', data=data,
                                    format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        correct_response = b'{"description":["This field may not be blank."]}'
        self.assertEqual(response.content, correct_response)

    def test_service_request_missing_email_field(self):
        data = {"name": "FooName",
                "description": "foodescription"}
        response = self.client.post('/api/service_request/', data=data,
                                    format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        correct_response = b'{"email":["This field is required."]}'
        self.assertEqual(response.content, correct_response)

    def test_service_request_missing_name_field(self):
        data = {"email": "fooo@gmail.com",
                "description": "foodescription"}
        response = self.client.post('/api/service_request/', data=data,
                                    format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        correct_response = b'{"name":["This field is required."]}'
        self.assertEqual(response.content, correct_response)

    def test_service_request_missing_description_field(self):
        data = {"name": "Fooname",
                "email": "fooo@gmail.com"}
        response = self.client.post('/api/service_request/', data=data,
                                    format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        correct_response = b'{"description":["This field is required."]}'
        self.assertEqual(response.content, correct_response)

    def test_service_request_saving_file(self):
        data = {"name": "Fooname",
                "email": "fooo@gmail.com",
                "description": "foodescription",
                "file": open(self.file_path, 'rb')}
        response = self.client.post('/api/service_request/', data=data,
                                    format='multipart')
        data.pop('file')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data, data)
        saved_file = File.objects.last()
        self.assertEqual(saved_file.service.email, "fooo@gmail.com")
        saved_file.service.delete()
        saved_file.delete()

    def test_service_request_saving_several_files(self):
        data = {"name": "Fooname",
                "email": "fooo@gmail.com",
                "description": "foodescription",
                "file1": open(self.file_path, 'rb'),
                "file2": open(self.file_pdf_path, 'rb')}
        response = self.client.post('/api/service_request/', data=data,
                                    format='multipart')
        data.pop('file1')
        data.pop('file2')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data, data)
        saved_file = File.objects.last()
        self.assertEqual(saved_file.service.email, "fooo@gmail.com")
        saved_file.delete()
        saved_file = File.objects.last()
        self.assertEqual(saved_file.service.email, "fooo@gmail.com")
        saved_file.service.delete()
        saved_file.delete()
