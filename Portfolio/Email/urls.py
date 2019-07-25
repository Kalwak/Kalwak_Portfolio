from .views import SendEmail
from django.urls import path

urlpatterns = [
    path('SendEmail', SendEmail, name='SendEmail'),
]
