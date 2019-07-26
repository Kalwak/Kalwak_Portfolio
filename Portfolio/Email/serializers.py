from rest_framework import serializers
from django.core.mail import EmailMessage
from django.conf import settings


class EmailSerializer(serializers.Serializer):
    subject = serializers.CharField(max_length=50, allow_blank=False)
    email = serializers.EmailField(allow_blank=False)
    message = serializers.CharField(max_length=1000, allow_blank=False)

    def send_email(self):
        to_email = settings.DEFAULT_FROM_EMAIL
        email = EmailMessage(self.data['subject'],
                             '%s \n From %s' % (self.data['message'],
                                                self.data['email']),
                             to=[to_email])
        response = email.send()
        return response
