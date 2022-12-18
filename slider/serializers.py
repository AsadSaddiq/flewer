from rest_framework import serializers
from slider.models import SliderImages


class ImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = SliderImages
        fields = '__all__'
        

