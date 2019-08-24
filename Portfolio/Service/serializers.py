from rest_framework import serializers
from .models import ServiceRequest as ServiceR
from .models import File
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
import logging
log = logging.getLogger('debugger')


class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = '__all__'


class ServiceRequestSerializer(serializers.HyperlinkedModelSerializer):
    files = FileSerializer(source='servicefile_set', many=True,
                           read_only=True)

    class Meta:
        model = ServiceR
        fields = ('name', 'email', 'description', 'files')

    def create(self, validated_data):
        """
        Create method overrided to save several files from the same request
        and send an email to website owners.
        """
        files_data = self.context['request'].FILES
        service = ServiceR.objects.create(**validated_data)
        for file_data in files_data.values():
            File.objects.create(service=service, file=file_data)
            log.info('File ' + file_data.name + ' created and attached to ' +
                     service.name + ' service')
        html_email = render_to_string('basic.html', validated_data)
        plain_email = strip_tags(html_email)
        to_email = settings.SERVER_EMAIL
        email = EmailMultiAlternatives("Kalwak: Service Request",
                                       plain_email, to_email,
                                       [to_email])
        email.attach_alternative(html_email, "text/html")

        for file in File.objects.filter(service=service):
            email.attach_file(file.file.path)

        email.send()

        return validated_data


class ChatbotSerializer(serializers.Serializer):
    """
    Does not need to override the update or create methods since this is used only to validate that the JSON sent to the
    ChatbotAPIView is valid.
    """
    msg = serializers.CharField()
    ip = serializers.IPAddressField()
