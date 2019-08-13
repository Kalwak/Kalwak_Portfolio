from .views import ServiceRequestView
from django.urls import path

urlpatterns = [
    path('service_request/', ServiceRequestView.as_view({'post': 'create'}),
         name='service_request')
]
