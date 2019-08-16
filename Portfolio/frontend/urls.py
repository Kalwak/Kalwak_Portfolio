from django.urls import path
from frontend.views import VuejsFrontend

urlpatterns = (
    path('', VuejsFrontend.as_view()),
)
