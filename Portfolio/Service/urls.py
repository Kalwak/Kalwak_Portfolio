from Service.views import ChatbotAPIView, GetIP
from .views import ServiceRequestView
from django.urls import path

app_name = 'service'

urlpatterns = [
    path('service_request/', ServiceRequestView.as_view({'post': 'create'}),
         name='service_request'),
    path('chatbot/', ChatbotAPIView.as_view(), name="chatbot"),
    path('get-ip/', GetIP.as_view(), name="get-ip"),
]
