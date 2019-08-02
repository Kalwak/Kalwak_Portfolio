from django.test import TestCase, override_settings
from rest_framework.test import APIClient
from rest_framework import status
from Proyect.models import Logs


class LogsTestCase(TestCase):

    def setUp(self) -> None:
        self.client = APIClient()

    def test_log_creation(self):
        self.client.get("/api/send_email")
        expected = 1
        log = Logs.objects.all().first()
        log_count = Logs.objects.all().count()
        self.assertEqual(expected, log_count)
        log_status_code = log.status_code
        expected = status.HTTP_405_METHOD_NOT_ALLOWED
        self.assertEqual(expected, log_status_code)

    def test_log_404(self):
        self.client.get("/fakeurl/")
        expected = status.HTTP_404_NOT_FOUND
        status_code = Logs.objects.last().status_code
        self.assertEqual(expected, status_code)

    def test_log_200(self):
        data = {
            "ok": 1
        }
        self.client.post("/api/send_email", data=data, content_type="application/json")
        status_code = Logs.objects.last().status_code
        expected = status.HTTP_400_BAD_REQUEST
        self.assertEqual(expected, status_code)

    def create_10_logs(self):
        for _ in range(10):
            self.client.get("/fakeurl/")

    @override_settings(LOGS_LIMIT=10)
    def test_limit_logs1(self):
        self.create_10_logs()
        amount = Logs.objects.count()
        expected = 10
        self.assertEqual(amount, expected)
        self.create_10_logs()
        amount = Logs.objects.count()
        expected = 10
        self.assertEqual(amount, expected)

