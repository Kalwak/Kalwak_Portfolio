from .models import ServiceRequest
from rest_framework import viewsets
from .serializers import ServiceRequestSerializer
from rest_framework import status
from rest_framework.response import Response
from Portfolio import logging_debugger as log


class ServiceRequestView(viewsets.ModelViewSet):
    serializer_class = ServiceRequestSerializer
    queryset = ServiceRequest.objects.all()

    def create(self, request, *args, **kwargs):
        """
        Post Method that saves a ServiceRequest
        :params request: should contain a JSON with name, email and description
                        also, could have attached several files.
        """
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        if serializer.is_valid():
            log.info('Request data is valid.')
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        log.info('Request data is not valid.')
        return Response(serializer.errors)
