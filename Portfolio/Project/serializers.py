from rest_framework import serializers
from . import models


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Project
        fields = '__all__'


class GallerySerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Gallery
        fields = '__all__'
