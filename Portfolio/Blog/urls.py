from django.urls import path

from Blog.views import BlogListView
from .views import BlogView

app_name = 'blog'

urlpatterns = [
    path('blog/', BlogView.as_view({"post": "create"}),
         name='blog'),
    path('blog/<int:pk>/', BlogView.as_view({"get": "retrieve"}),
         name='blog_retrieve'),
    path('blog-list/', BlogListView.as_view(),
         name='blog_list')
]
