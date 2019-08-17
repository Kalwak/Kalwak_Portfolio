from .serializers import EmailSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from Portfolio import log


class SendEmailView(viewsets.ViewSet):

    def create(self, request):
        """
        Post Method that sends an Email from the 'Contact us' page form
        to the group Email.
        :params request: should contain a JSON with email,subject and message
        """
        serializer = EmailSerializer(data=request.data)
        if serializer.is_valid():
            log.info('Request data is valid.')
            response = serializer.send_email()
            return Response({"response": response})
        log.info('Request data is not valid.')
        return Response(serializer.errors)
