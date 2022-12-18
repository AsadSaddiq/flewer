from rest_framework import serializers
from .models import PaymentHistory

class P_historySerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentHistory
        fields = '__all__'

