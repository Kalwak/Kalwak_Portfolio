from rest_framework import serializers
from . import models

class ProyectSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Proyect
        fields = ("name", "date", "description")


class GallerySerializers(serializers.ModelSerializer):
	class Meta:
		model = models.Gallery
		fields = '__all__'