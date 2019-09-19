from rest_framework import viewsets, status
from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from Blog.serializers import BlogListSerializer, BlogFilterSerializer
from .serializers import BlogSerializer
from .models import Blog


class StandardResultsSetPagination(PageNumberPagination):
    """
    A paginator that gives 6 elements at a time
    """
    page_size = 6
    page_size_query_param = 'page_size'
    max_page_size = 6


class BlogListView(ListAPIView):
    """
    A paginator view for blogs giving 6 by 6 and with a serializer
    that gives all of the Blogs' fields but the text field
    """
    queryset = Blog.objects.all()
    serializer_class = BlogListSerializer
    pagination_class = StandardResultsSetPagination

    def get(self, request, *args, **kwargs):
        params = dict(request.query_params)
        params.pop("page")
        for param in params:
            params[param] = "".join(params[param])
        serializer = BlogFilterSerializer(data=params)

        if params:
            if serializer.is_valid():
                if "tag" in serializer.validated_data:
                    self.queryset = self.queryset.filter(tag=serializer.validated_data.get("tag"))
                if "year" in serializer.validated_data:
                    self.queryset = self.queryset.filter(date__year=serializer.validated_data.get("year"))
                if "month" in serializer.validated_data:
                    self.queryset = self.queryset.filter(date__month=serializer.validated_data.get("month"))
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        return super(BlogListView, self).list(request, *args, **kwargs)


class BlogView(viewsets.ModelViewSet):
    """
    Blog viewset. It allow you to perform Get and Post methods.
    With GET method it can give you the list of Blogs or you can retrieve
    individual Blogs.
    """
    serializer_class = BlogSerializer
    queryset = Blog.objects.all()
