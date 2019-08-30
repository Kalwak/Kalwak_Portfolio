from rest_framework import viewsets
from .serializers import BlogSerializer
from .models import Blog


class BlogView(viewsets.ModelViewSet):
    """
    Blog viewset. It allow you to perform Get and Post methods.
    With GET method it can give you the list of Blogs or you can retrieve
    individual Blogs.
    """
    serializer_class = BlogSerializer
    queryset = Blog.objects.all()
