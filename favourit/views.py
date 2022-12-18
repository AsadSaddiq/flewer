from django.shortcuts import render
from .models import FavouritHotel, FavouritHostel, FavouritHouse, FavouritGuider, FavouritTripComp
from .serializers import FavHotelSerializer , FavHostelSerializer, FavHouseSerializer, FavGuiderSerializer, FavTripCompSerializer
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response



# /////////////////////////////HOTEL/////////////////////////////

class favhotelcreate(APIView):
  def post(self, request,  format=None):
    serializer = FavHotelSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)


class favhotelRetrieve(APIView):
  def get(self, request, pk=None, format=None):
    id = pk
    if id is not None:
      stu = FavouritHotel.objects.filter(hotel=id)
      serializer = FavHotelSerializer(stu, many=True)
      return Response(serializer.data)
    

class favhotelDestroy(APIView):
  # permission_classes = [IsAuthenticated]
  def delete(self, request, hotel, owner=None):
    stu = FavouritHotel.objects.get(id_no=hotel, hotel=owner)
    stu.delete()
    return Response({'msg': 'deleted'})





# /////////////////////////////HOSTEL/////////////////////////////

class favhostelcreate(APIView):
  def post(self, request,  format=None):
    serializer = FavHostelSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)


class favhostelRetrieve(APIView):
  def get(self, request, pk=None, format=None):
    id = pk
    if id is not None:
      stu = FavouritHostel.objects.filter(hostel=id)
      serializer = FavHostelSerializer(stu, many=True)
      return Response(serializer.data)
    

class favhostelDestroy(APIView):
  # permission_classes = [IsAuthenticated]
  def delete(self, request, hostel, owner):
    stu = FavouritHostel.objects.get(id_no=hostel, hostel=owner)
    stu.delete()
    return Response({'msg': 'deleted'})






# /////////////////////////////HOUSE/////////////////////////////

class favhousecreate(APIView):
  def post(self, request,  format=None):
    serializer = FavHouseSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)


class favhouseRetrieve(APIView):
  def get(self, request, pk=None, format=None):
    id = pk
    if id is not None:
      stu = FavouritHouse.objects.filter(house=id)
      serializer = FavHouseSerializer(stu, many=True)
      return Response(serializer.data)
    

class favhouseDestroy(APIView):
  permission_classes = [IsAuthenticated]
  def delete(self, request, house, owner):
    stu = FavouritHouse.objects.get(id_no=house, house=owner)
    stu.delete()
    return Response({'msg': 'deleted'})




    

# /////////////////////////   TRIP    /////////////////////////////

class favTripCompcreate(APIView):
  def post(self, request,  format=None):
    serializer = FavTripCompSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)


class favTripCompRetrieve(APIView):
  def get(self, request, pk=None, format=None):
    id = pk
    if id is not None:
      stu = FavouritTripComp.objects.filter(tripComp=id)
      serializer = FavTripCompSerializer(stu, many=True)
      return Response(serializer.data)
    

class favTripCompDestroy(APIView):
  permission_classes = [IsAuthenticated]
  def delete(self, request, comp, owner):
    stu = FavouritTripComp.objects.get(id_no=comp, tripComp=owner)
    stu.delete()
    return Response({'msg': 'deleted'})








# ////////////////////////   GUIDER   /////////////////////////////


class favGuidercreate(APIView):
  def post(self, request,  format=None):
    serializer = FavGuiderSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)


class favGuiderRetrieve(APIView):
  def get(self, request, pk=None, format=None):
    id = pk
    if id is not None:
      stu = FavouritGuider.objects.filter(guider=id)
      serializer = FavGuiderSerializer(stu, many=True)
      return Response(serializer.data)
    

class favGuiderDestroy(APIView):
  permission_classes = [IsAuthenticated]
  def delete(self, request, guider, owner):
    stu = FavouritGuider.objects.get(id_no=guider, guider=owner)
    stu.delete()
    return Response({'msg': 'deleted'})