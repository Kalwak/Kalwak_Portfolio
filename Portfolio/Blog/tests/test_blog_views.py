import tempfile

from PIL import Image
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from Blog.models import Blog
from django.utils import timezone


class BlogTestCase(TestCase):
    tmp_file = None

    def setUp(self) -> None:
        self.client = APIClient()
        image = Image.new('RGB', (100, 100))

        self.tmp_file = tempfile.NamedTemporaryFile(suffix='.jpg')
        image.save(self.tmp_file)
        self.tmp_file.seek(0)

    def test_blog_post_successful(self):
        data = {"title": "A Wonderful Test",
                "author": "Tester",
                "tag": "startup",
                "text": "This is my blog.",
                "thumbnail": self.tmp_file}
        response = self.client.post('/api/blog/', data=data,
                                    format='multipart')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        response.data.pop('date')
        self.assertEqual(response.data["text"], data['text'])

    def test_blog_get_successful(self):
        response = self.client.get('/api/get/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_blog_retrive_succesful(self):
        Blog.objects.create(
            id=1,
            title="Finding the perfect test",
            author="Tester",
            tag="Startup",
            text="TEST TEXT"
        )
        path = '/api/blog/1/'
        response = self.client.get(path)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_blog_post_missing_title_field(self):
        data = {"author": "Tester",
                "tag": "startup",
                "text": "This is my blog.",
                "thumbnail": self.tmp_file}
        response = self.client.post('/api/blog/', data=data,
                                    format='multipart')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        correct_response = b'{"title":["This field is required."]}'
        self.assertEqual(response.content, correct_response)

    def test_blog_post_missing_author_field(self):
        data = {"title": "Tester",
                "tag": "startup",
                "text": "This is my blog.",
                "thumbnail": self.tmp_file}
        response = self.client.post('/api/blog/', data=data,
                                    format='multipart')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        correct_response = b'{"author":["This field is required."]}'
        self.assertEqual(response.content, correct_response)

    def test_blog_post_missing_text_field(self):
        data = {"title": "Test Title",
                "author": "Tester",
                "tag": "startup",
                "thumbnail": self.tmp_file}
        response = self.client.post('/api/blog/', data=data,
                                    format='multipart')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        correct_response = b'{"text":["This field is required."]}'
        self.assertEqual(response.content, correct_response)

    def test_blog_post_missing_tag_field(self):
        data = {"title": "A Wonderful Test",
                "author": "Tester",
                "text": "This is my blog.",
                "thumbnail": self.tmp_file}
        response = self.client.post('/api/blog/', data=data,
                                    format='multipart')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        correct_response = b'{"tag":["This field is required."]}'
        self.assertEqual(response.content, correct_response)

    def test_blog_post_date_added(self):
        data = {"title": "A Wonderful Test",
                "author": "Tester",
                "tag": "startup",
                "text": "This is my blog.",
                "date": "01/01/2019",
                "thumbnail": self.tmp_file}
        response = self.client.post('/api/blog/', data=data,
                                    format='multipart')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        # The date here must be different from the one sended in the post.
        self.assertEqual(response.data['date'], str(timezone.localdate()))
