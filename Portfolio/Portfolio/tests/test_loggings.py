from django.test import TestCase
from rest_framework.test import APIClient
from Portfolio.settings import BASE_DIR
from Portfolio import log
import os


class LoggingTests(TestCase):

    def setUp(self) -> None:
        self.client = APIClient()
        self.error_path = os.path.join(BASE_DIR, 'logs/errors.log')
        self.debug_path = os.path.join(BASE_DIR, 'logs/debug.log')

    def test_debug_file_exists(self):
        self.assertEquals(os.path.exists(self.debug_path), True)

    def test_error_file_exists(self):
        self.assertEquals(os.path.exists(self.error_path), True)

    def test_error_file_writes_404(self):
        self.client.get("/fakeurl/")
        # opening the log_file
        file = open(self.error_path, "r")
        log_file = file.readlines()
        # getting last log
        last_request = log_file[len(log_file)-2]
        file.close()
        # verifying http status
        http_status_last_request = last_request.split()[-1]
        self.assertEqual(http_status_last_request, "404")
        # verifying url from the request
        url_last_request = last_request.split()[-3]
        self.assertEqual(url_last_request, "/fakeurl/")

    def test_debug_file_writes(self):
        log.info('Testing')
        # opening the log_file
        file = open(self.debug_path, "r")
        log_file = file.readlines()
        # getting last log
        last_request = log_file[len(log_file)-1]
        file.close()
        # verifying log writes
        info_logged = last_request.split()[-1]
        self.assertEqual(info_logged, "Testing")
        # verifying correct log level
        info_logged = last_request.split()[0]
        self.assertEqual(info_logged, "INFO")
