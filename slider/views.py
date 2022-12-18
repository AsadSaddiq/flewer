from django.shortcuts import render
from rest_framework.views import APIView
from slider.models import SliderImages
from .serializers import ImagesSerializer
from rest_framework.response import Response


class ImagesRetrieve(APIView):
  def get(self, request, pk=None, format=None):
    id = pk
    if id is not None:
      stu = SliderImages.objects.filter(id=id)
      serializer = ImagesSerializer(stu, many=True)
      return Response(serializer.data)
    stu = SliderImages.objects.all()
    serializer = ImagesSerializer(stu, many=True)
    return Response(serializer.data)