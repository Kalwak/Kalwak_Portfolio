from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status


class EmailTestCase(TestCase):

    def setUp(self) -> None:
        self.client = APIClient()

    def test_send_mail_post_successful(self):
        data = {'subject': 'Test Kalwak Email API',
                'message': 'This is a test',
                'email': 'kalwakcr@gmail.com'}
        response = self.client.post('/api/send_email', data=data,
                                    format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        correct_data_response = {'response': 1}
        self.assertEqual(response.data, correct_data_response)

    def test_send_mail_post_incorrect_email(self):
        data = {'subject': 'Test Kalwak Email API',
                'message': 'This is a test',
                'email': 'kalwakcrgmail.com'}
        response = self.client.post('/api/send_email', data=data,
                                    format='json')
        correct_response = b'{"email":["Enter a valid email address."]}'
        self.assertEqual(response.content, correct_response)

    def test_send_mail_post_missing_message_field(self):
        data = {'subject': 'Test Kalwak Email API',
                'email': 'kalwakcr@gmail.com'}
        response = self.client.post('/api/send_email', data=data,
                                    format='json')
        correct_response = b'{"message":["This field is required."]}'
        self.assertEqual(response.content, correct_response)

    def test_send_mail_post_missing_subject_field(self):
        data = {'message': 'This is a test',
                'email': 'kalwakcr@gmail.com'}
        response = self.client.post('/api/send_email', data=data,
                                    format='json')
        correct_response = b'{"subject":["This field is required."]}'
        self.assertEqual(response.content, correct_response)

    def test_send_mail_post_missing_email_field(self):
        data = {'subject': 'Test Kalwak Email API',
                'message': 'This is a test'}
        response = self.client.post('/api/send_email', data=data,
                                    format='json')
        correct_response = b'{"email":["This field is required."]}'
        self.assertEqual(response.content, correct_response)

    def test_send_mail_get(self):
        response = self.client.get("/api/send_email")
        status_expected = status.HTTP_405_METHOD_NOT_ALLOWED
        self.assertEqual(response.status_code, status_expected)
