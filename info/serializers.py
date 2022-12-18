from rest_framework import serializers
from .models import PrivecyPolicy, TermService

class PrivecyPolicySerializer(serializers.ModelSerializer):
    class Meta:
        model = PrivecyPolicy
        fields = '__all__'


class TermServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = TermService
        fields = '__all__'