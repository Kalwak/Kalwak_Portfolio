from rest_framework import serializers
from .models import ServiceRequest as ServiceR
from .models import File
from Portfolio import log


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
        files_data = self.context['request'].FILES
        service = ServiceR.objects.create(**validated_data)
        for file_data in files_data.values():
            File.objects.create(service=service, file=file_data)
            log.info('File ' + file_data.name + ' created and attached to ' +
                     service.name + ' service')
        return validated_data
