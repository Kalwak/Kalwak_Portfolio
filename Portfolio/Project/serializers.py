from rest_framework import serializers
from . import models


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Project
        fields = ("name", "date", "description")


class GallerySerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Gallery
        fields = '__all__'
