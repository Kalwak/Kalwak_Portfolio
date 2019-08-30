from django.urls import path
from .views import BlogView

app_name = 'blog'

urlpatterns = [
    path('blog/', BlogView.as_view({"get": "list", "post": "create"}),
         name='blog'),
    path('blog/<int:pk>/', BlogView.as_view({"get": "retrieve"}),
         name='blog_retrieve'),
]
