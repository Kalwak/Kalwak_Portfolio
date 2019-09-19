from rest_framework import viewsets
from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination

from Blog.serializers import BlogListSerializer
from .serializers import BlogSerializer
from .models import Blog


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 6
    page_size_query_param = 'page_size'
    max_page_size = 6


class BlogListView(ListAPIView):
    """

    """
    queryset = Blog.objects.all()
    serializer_class = BlogListSerializer
    pagination_class = StandardResultsSetPagination


class BlogView(viewsets.ModelViewSet):
    """
    Blog viewset. It allow you to perform Get and Post methods.
    With GET method it can give you the list of Blogs or you can retrieve
    individual Blogs.
    """
    serializer_class = BlogSerializer
    queryset = Blog.objects.all()
