import json
import requests
import re
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient
from django.urls import reverse
from random import getrandbits
from ipaddress import IPv4Address


class ChatbotTests(TestCase):
    url = ""

    def generate_random_ip(self) -> str:
        bits = getrandbits(32)  # generates an integer with 32 random bits
        addr = IPv4Address(bits)  # instances an IPv4Address object from those bits
        addr_str = str(addr)  # get the IPv4Address object's string representation
        return addr_str

    def remove_extra_double_quotes(self, string: str) -> str:
        if string[0] == "\"":
            string = string[1:]
        if string[-1] == "\"":
            string = string[:len(string) - 1]
            if string[-1] == "\\":
                string = string[:len(string) - 1]

        return string

    def setUp(self) -> None:
        self.client = APIClient()
        self.url = reverse("service:chatbot")

    def test_ip_generator(self):
        ip = self.generate_random_ip()
        regex = re.compile(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$")
        match = regex.match(ip)
        self.assertTrue(match is not None)

    def test_400_msg(self):
        data = {
            "msg": "Hi",
            "ip": "1"
        }
        response = self.client.post(self.url, data=data)
        response = json.loads(response.content)
        expected_status = 400
        expected = "Enter a valid IPv4 or IPv6 address."
        self.assertEqual(expected, response["ip"][0])
        self.assertEqual(expected_status, status.HTTP_400_BAD_REQUEST)

    def test_400_required(self):
        data = {
            "msg": "Hi"
        }
        response = self.client.post(self.url, data=data)
        response = json.loads(response.content)
        expected_status = 400
        expected = "This field is required."
        self.assertEqual(expected, response["ip"][0])
        self.assertEqual(expected_status, status.HTTP_400_BAD_REQUEST)

        data = {
            "ip": self.generate_random_ip()
        }
        response = self.client.post(self.url, data=data)
        response = json.loads(response.content)
        expected_status = 400
        expected = "This field is required."
        self.assertEqual(expected, response["msg"][0])
        self.assertEqual(expected_status, status.HTTP_400_BAD_REQUEST)

    def test_get_put_delete_patch_methods(self):
        expected_status = 405

        response = self.client.get(self.url)
        self.assertEqual(response.status_code, expected_status)

        response = self.client.put(self.url)
        self.assertEqual(response.status_code, expected_status)

        response = self.client.delete(self.url)
        self.assertEqual(response.status_code, expected_status)

        response = self.client.patch(self.url)
        self.assertEqual(response.status_code, expected_status)

    def test_chatbot_output1(self):
        ip = self.generate_random_ip()
        data = {
            "msg": "WHAT IS MY NAME",
            "ip": ip,
            "current_vue_path": "/"
        }
        response = self.client.post(self.url, data=data)
        response = response.content.decode().replace("\"", "")
        expected = "You never told me your name."
        self.assertEqual(response, expected)

        data = {
            "msg": "My name is Joseph",
            "ip": ip,
            "current_vue_path": "/"
        }
        response = self.client.post(self.url, data=data)
        response = response.content.decode().replace("\"", "")
        expected = ["Nice to meet you, Joseph.", "Joseph, nice to meet you."]
        self.assertIn(response, expected)

        data = {
            "msg": "WHAT IS MY NAME",
            "ip": ip,
            "current_vue_path": "/"
        }
        response = self.client.post(self.url, data=data)
        response = response.content.decode().replace("\"", "")
        expected = [
            "Your name is Joseph.",
            "You told me your name is Joseph.",
            "Aren't you Joseph?"
        ]
        self.assertIn(response, expected)

    def test_chatbot_output2(self):
        ip = self.generate_random_ip()
        data = {
            "msg": "RANDOM TESTING TEXT",
            "ip": ip,
            "current_vue_path": "/"
        }
        response = self.client.post(self.url, data=data)
        response = response.content.decode().replace("\"", "")
        expected = ["I didn't quite understand.", "Sorry, I do not understand."]
        self.assertIn(response, expected)

        data = {
            "msg": "mY naMe IS Jose",
            "ip": ip,
            "current_vue_path": "/"
        }
        response = self.client.post(self.url, data=data)
        response = response.content.decode().replace("\"", "")
        expected = ["Nice to meet you, Jose.", "Jose, nice to meet you."]
        self.assertIn(response, expected)

    def test_chatbot_output3(self):
        ip = self.generate_random_ip()
        data = {
            "msg": "Hi",
            "ip": ip,
            "current_vue_path": "/"
        }
        response = self.client.post(self.url, data=data)
        response = response.content.decode().replace("\"", "")
        expected = "Greetings"
        self.assertTrue(expected in response)

        data = {
            "msg": "Edwin",
            "ip": ip,
            "current_vue_path": "/"
        }
        response = self.client.post(self.url, data=data)
        response = response.content.decode().replace("\"", "")
        expected = ["Nice to meet you, Edwin.", "Edwin, nice to meet you."]
        self.assertIn(response, expected)

    def test_chatbot_output4(self):
        ip2 = self.generate_random_ip()
        data = {
            "msg": "Hi",
            "ip": ip2,
            "current_vue_path": "/"
        }
        response = self.client.post(self.url, data=data)
        response = response.content.decode().replace("\"", "")
        expected = "Greetings"
        self.assertTrue(expected in response)

        data = {
            "msg": "Edwin",
            "ip": ip2,
            "current_vue_path": "/"
        }
        response = self.client.post(self.url, data=data)
        response = response.content.decode().replace("\"", "")
        expected = ["Nice to meet you, Edwin.", "Edwin, nice to meet you."]
        self.assertIn(response, expected)

        ip1 = self.generate_random_ip()
        data = {
            "msg": "my name is Jennifer",
            "ip": ip1,
            "current_vue_path": "/"
        }
        response = self.client.post(self.url, data=data)
        response = response.content.decode().replace("\"", "")
        expected = ["Nice to meet you, Jennifer.", "Jennifer, nice to meet you."]
        self.assertIn(response, expected)

        expected = "Jennifer"
        data = {
            "msg": "Who am I?",
            "ip": ip1,
            "current_vue_path": "/"
        }
        response = self.client.post(self.url, data=data)
        response = response.content.decode().replace("\"", "")
        self.assertIn(expected, response)

        expected = "Edwin"
        data = {
            "msg": "Who am I?",
            "ip": ip2,
            "current_vue_path": "/"
        }
        response = self.client.post(self.url, data=data)
        response = response.content.decode().replace("\"", "")
        self.assertIn(expected, response)

    def test_chatbot_output5(self):
        ip = self.generate_random_ip()
        data = {
            "msg": "What are your services?",
            "ip": ip,
            "current_vue_path": "/"
        }
        response = self.client.post(self.url, data=data)
        response = response.content.decode().replace("\"", "")
        expected = "Services</a>"
        self.assertIn(expected, response)

    def test_chatbot_output6(self):
        ip = self.generate_random_ip()
        data = {
            "msg": "Do you guys provide us with web development??",
            "ip": ip,
            "current_vue_path": "/"
        }
        response = self.client.post(self.url, data=data)
        response = response.content.decode()
        expected = "Services</a>"
        self.assertIn(expected, response)

    def test_chatbot_output_test_links(self):
        ip = self.generate_random_ip()
        data = {
            "msg": "facebook",
            "ip": ip,
            "current_vue_path": "/"
        }
        response = self.client.post(self.url, data=data)
        response = response.content.decode()
        response = self.remove_extra_double_quotes(response)

        regex = r"\".*\">facebook"
        match = re.findall(regex, response)[0]
        match = match.replace(">facebook", "")
        match = self.remove_extra_double_quotes(match)

        result = requests.get(match)

        expected = 200

        self.assertEqual(expected, result.status_code)
        data = {
            "msg": "what are your products you sell",
            "ip": ip,
            "current_vue_path": "/"
        }
        response = self.client.post(self.url, data=data)
        response = response.content.decode()
        response = self.remove_extra_double_quotes(response)

        match = re.findall(regex, response)[0]
        match = match.replace(">facebook", "")
        match = self.remove_extra_double_quotes(match)

        result = requests.get(match)

        expected = 200
        self.assertEqual(expected, result.status_code)

    def test_chatbot_output7(self):
        ip = self.generate_random_ip()
        data = {
            "msg": "give me a way to contact your developers",
            "ip": ip,
            "current_vue_path": "/path1/"
        }
        response = self.client.post(self.url, data=data)
        response = response.content.decode()
        response = self.remove_extra_double_quotes(response)
        expected = 'Send a message to +50684599023, an email to kalwakcr@gmail.com or go to our contact-us section <a href=\\"/path1/#contact-section\\"> Contact</a>'
        self.assertEqual(expected, response)

    def test_chatbot_output8(self):
        ip = self.generate_random_ip()
        data = {
            "msg": "info",
            "ip": ip,
            "current_vue_path": "/"
        }
        response = self.client.post(self.url, data=data)
        response = response.content.decode().replace("\"", "")
        expected = 'Kalwak is a company'
        self.assertIn(expected, response)

    def test_chatbot_output9(self):
        ip = self.generate_random_ip()
        data = {
            "msg": "tell me about de development team",
            "ip": ip,
            "current_vue_path": "/"
        }
        response = self.client.post(self.url, data=data)
        response = response.content.decode().replace("\"", "")
        expected = 'amazing software UI'
        self.assertIn(expected, response)
