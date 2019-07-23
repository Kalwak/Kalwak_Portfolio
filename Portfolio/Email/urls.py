from .views import SendEmail, EmailListView
from django.urls import path

urlpatterns = [
    path('SendEmail', SendEmail, name='SendEmail'),
    path('EmailListView', EmailListView.as_view(), name='EmailListView'),
]
