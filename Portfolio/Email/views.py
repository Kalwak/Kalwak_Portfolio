from .serializers import EmailSerializer
from rest_framework import viewsets
from rest_framework.response import Response


class SendEmailView(viewsets.ViewSet):

    def create(self, request):
        """
        Post Method that sends an Email from the 'Contact us' page form
        to the group Email.
        :params request: should contain a JSON with email,subject and message
        """
        serializer = EmailSerializer(data=request.data)
        if serializer.is_valid():
            response = serializer.send_email()
            return Response({"response": response})
        return Response(serializer.errors)
