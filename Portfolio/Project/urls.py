from django.urls import path
from Project.views import ProjectViewset

urlpatterns = (
    path('project/', ProjectViewset.as_view({"get": "list"})),
    path('project/<int:pk>/', ProjectViewset.as_view({"get": "retrieve"})),
)
