from rest_framework import serializers
from django.core.files.base import ContentFile
from .models import ServiceRequest as ServiceR
from .models import Files


class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Files
        fields = '__all__'


class ServiceRequestSerializer(serializers.HyperlinkedModelSerializer):
    files = FileSerializer(source='servicefile_set', many=True,
                           read_only=True)

    class Meta:
        model = ServiceR
        fields = ('name', 'email', 'description', 'files')

    def create(self, validated_data):
        files_data = self.context['request'].FILES
        service = ServiceR.objects.create(**validated_data)
        for file_data in files_data.values():
            Files.objects.create(service=service, file=file_data)
        return validated_data
