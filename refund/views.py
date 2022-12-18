from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Refund
from .serializers import RefundSerializer

class RefundRetrieve(APIView):
#   permission_classes = [IsAuthenticated]
  def get(self, request, format=None):
    stu = Refund.objects.all()
    serializer = RefundSerializer(stu, many=True)
    return Response(serializer.data)