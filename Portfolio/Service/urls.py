from Service.views import ChatbotAPIView
from .views import ServiceRequestView
from django.urls import path

app_name = 'service'

urlpatterns = [
    path('service_request/', ServiceRequestView.as_view({'post': 'create'}),
         name='service_request'),
    path('chatbot/', ChatbotAPIView.as_view(), name="chatbot")
]
