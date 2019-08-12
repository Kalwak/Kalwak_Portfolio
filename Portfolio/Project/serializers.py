from rest_framework import serializers
from . import models


class GallerySerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Gallery
        fields = '__all__'


class ProjectSerializer(serializers.ModelSerializer):
    images = GallerySerializers(many=True)

    class Meta:
        model = models.Project
        fields = ["name", "cover_page", "description", "website", "date", "subtitle", "categories", "images"]
