from .views import SendEmailView
from django.urls import path

app_name = 'email'

urlpatterns = [
    path('send_email/', SendEmailView.as_view({'post': 'create'}),
         name='send_email'),
]
