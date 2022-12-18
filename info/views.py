from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import PrivecyPolicy, TermService
from .serializers import PrivecyPolicySerializer, TermServiceSerializer

class PrivecyPolicyRetrieve(APIView):
#   permission_classes = [IsAuthenticated]
  def get(self, request, format=None):
    stu = PrivecyPolicy.objects.all()
    serializer = PrivecyPolicySerializer(stu, many=True)
    return Response(serializer.data)



class TermServiceRetrieve(APIView):
#   permission_classes = [IsAuthenticated]
  def get(self, request, format=None):
    stu = TermService.objects.all()
    serializer = TermServiceSerializer(stu, many=True)
    return Response(serializer.data)
