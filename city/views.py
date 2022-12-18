from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import City
from .serializers import CitySerializer

class CityRetrieve(APIView):
#   permission_classes = [IsAuthenticated]
  def get(self, request, pk=None, format=None):
    id = pk
    if id is not None:
        stu = City.objects.filter(city=id)
        serializer = CitySerializer(stu, many=True)
        return Response(serializer.data)
    stu = City.objects.all()
    serializer = CitySerializer(stu, many=True)
    return Response(serializer.data)

