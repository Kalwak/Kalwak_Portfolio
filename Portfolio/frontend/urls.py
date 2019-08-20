from django.urls import path
from frontend.views import VuejsFrontend

app_name = 'frontend'

urlpatterns = (
    path('', VuejsFrontend.as_view()),
)
