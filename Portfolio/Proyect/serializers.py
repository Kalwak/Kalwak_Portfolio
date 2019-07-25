from rest_framework import serializers
from . import models

class ProyectSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ProyectForm
        fields = ('name', "Date", "Description")


class GallerySerializers(serializers.ModelSerializer):
	class Meta:
		model = models.GalleryForm
		fields = '__all__'