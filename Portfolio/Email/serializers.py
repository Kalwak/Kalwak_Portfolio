from rest_framework import serializers
from django.core.mail import EmailMessage
from django.conf import settings
from Portfolio import logging_debugger as log


class EmailSerializer(serializers.Serializer):
    subject = serializers.CharField(max_length=50, allow_blank=False)
    email = serializers.EmailField(allow_blank=False)
    message = serializers.CharField(max_length=1000, allow_blank=False)

    def send_email(self) -> int:
        """
        Sends email using serialized data.
        Returns 1 if the operation is successful and 0 if it fails.
        """
        to_email = settings.DEFAULT_FROM_EMAIL
        email = EmailMessage(self.data['subject'],
                             '%s \n From %s' % (self.data['message'],
                                                self.data['email']),
                             to=[to_email])
        response = email.send()
        log.info('Sendgrid Response: ' + str(response))
        return response
