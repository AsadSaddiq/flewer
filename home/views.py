
from accounts.models import UserAccount
from .models import Hotel, HotelBooking, HotelImages, Room, RoomPhoto, Rating
from .serializers import HotelSerializer , HotelImagesSerializer, HotelRoomSerializer, RoomImagesSerializer, HotelBookingSerializer, RatingSerializer, ratingSerializer, HotelgetSerializer
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
import datetime
from rest_framework.parsers import JSONParser
import io


class hotelcreate(APIView):
#   renderer_classes = [UserRenderer]
  permission_classes = [IsAuthenticated]
  def post(self, request,  format=None):
    serializer = HotelSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)


class hotelUpdate(APIView):
#   renderer_classes = [UserRenderer]
  permission_classes = [IsAuthenticated]
  def put(self, request, pk, format=None):
    id=pk
    stu = Hotel.objects.get(id=id)
    serializer = HotelSerializer(stu, data=request.data, partial=True)
    if serializer.is_valid():
     serializer.save()
     return Response(serializer.data)
    return Response(serializer.errors)


class hotelDestroy(APIView):
  permission_classes = [IsAuthenticated]
  def delete(self, request, pk, format=None):
    id = pk
    stu = Hotel.objects.get(id=pk)
    stu.delete()
    return Response({'msg': 'deleted'})


class hotelRetrieve(APIView):
#   permission_classes = [IsAuthenticated]
  def get(self, request, pk=None, format=None):
    id = pk
    if id is not None:
      stu = Hotel.objects.filter(user=id)
      serializer = HotelgetSerializer(stu, many=True)
      return Response(serializer.data)
    stu = Hotel.objects.all()
    serializer = HotelgetSerializer(stu, many=True)
    return Response(serializer.data)

class favhotelRetrieve(APIView):
#   permission_classes = [IsAuthenticated]
  def get(self, request, pk=None, format=None):
    id = pk
    if id is not None:
      stu = Hotel.objects.filter(id=id)
      serializer = HotelgetSerializer(stu, many=True)
      return Response(serializer.data)

# ////////////////////////    RATING API    ///////////////////

class RatingUpdate(APIView):
  # permission_classes = [IsAuthenticated]
  def put(self, request, pk, format=None):
    json_data = request.body
    stream = io.BytesIO(json_data)
    python_data = JSONParser().parse(stream)
    onestar = int(python_data.get('one'))
    twostar = int(python_data.get('two'))
    threestar = int(python_data.get('three'))
    fourstar = int(python_data.get('four'))
    fivestar = int(python_data.get('five'))

    id=pk
    stu = Hotel.objects.get(id=id)
    starone= int(stu.one)
    startwo= int(stu.two)
    starthree= int(stu.three)
    starfour= int(stu.four)
    starfive= int(stu.five)
    
    one= int(onestar + starone)
    two= int(twostar + startwo)
    three= int(threestar + starthree)
    four= int(fourstar + starfour)
    five= int(fivestar + starfive)
    mylist= {'one': one, 'two': two, 'three': three, 'four': four, 'five': five}
    print(one)
    print(two)
    print(three)
    serializer = RatingSerializer(stu, data=mylist, partial=True)
    if serializer.is_valid():
     serializer.save()
     return Response(serializer.data)
    return Response(serializer.errors)

class RatingHotel(APIView):
#   permission_classes = [IsAuthenticated]
  def get(self, request, pk=None, format=None):
    id = pk
    if id is not None:
      stu = Hotel.objects.filter(id=id)
      serializer = RatingSerializer(stu, many=True)
      return Response(serializer.data)


# /////////////////////  REVIEW  ///////////////////////////////

class Ratcreate(APIView):
  def post(self, request,  format=None):
    serializer = ratingSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)


class RatRetrieve(APIView):
#   permission_classes = [IsAuthenticated]
  def get(self, request, pk=None, format=None):
    id = pk
    if id is not None:
      stu = Rating.objects.filter(hotel=id)
      serializer = ratingSerializer(stu, many=True)
      return Response(serializer.data)
    stu = Rating.objects.all()
    serializer = ratingSerializer(stu, many=True)
    return Response(serializer.data)




class hotelImgapi(APIView):
#   permission_classes = [IsAuthenticated]
  def get(self, request, pk=None, format=None):
    id = pk
    if id is not None:
      stu = HotelImages.objects.filter(hotel=id)
      serializer = HotelImagesSerializer(stu, many=True)
      return Response(serializer.data)
    stu = HotelImages.objects.all()
    serializer = HotelImagesSerializer(stu, many=True)
    return Response(serializer.data)


class hotelImgaUpload(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request,  format=None):
        serializer = HotelImagesSerializer(data=request.data)
        if serializer.is_valid():
          serializer.save()
          return Response(serializer.data)
        return Response(serializer.errors)


class hotelImgapiDelete(APIView):
    permission_classes = [IsAuthenticated]
    def delete(self, request, pk, format=None):
        id = pk
        stu = Hotel.objects.get(id=pk)
        stu.delete()
        return Response({'msg': 'deleted'})




class RoomCreate(APIView):
#   renderer_classes = [UserRenderer]
  permission_classes = [IsAuthenticated]
  def post(self, request,  format=None):
    serializer = HotelRoomSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)




class RoomUpdate(APIView):
#   renderer_classes = [UserRenderer]
  permission_classes = [IsAuthenticated]
  def put(self, request, pk, format=None):
    id=pk
    stu = Room.objects.get(id=id)
    serializer = HotelRoomSerializer(stu, data=request.data, partial=True)
    if serializer.is_valid():
     serializer.save()
     return Response(serializer.data)
    return Response(serializer.errors)


class RoomDestroy(APIView):
  permission_classes = [IsAuthenticated]
  def delete(self, request, pk, format=None):
    id = pk
    stu = Room.objects.get(id=pk)
    stu.delete()
    return Response({'msg': 'deleted'})


class RoomRetrieve(APIView):
#   permission_classes = [IsAuthenticated]
  def get(self, request, pk=None, format=None):
    id = pk
    if id is not None:
        stu = Room.objects.filter(hotel=id)
        serializer = HotelRoomSerializer(stu, many=True)
        return Response(serializer.data)
    stu = Room.objects.all()
    serializer = HotelRoomSerializer(stu, many=True)
    return Response(serializer.data)

# ROOM IMAGES FUNCTIONS/////////////////////////////////////////////////////////

class roomImgapi(APIView):
    def get(self, request, pk=None, format=None):
      id = pk
      if id is not None:
        stu = RoomPhoto.objects.filter(room=id)
        serializer = RoomImagesSerializer(stu, many=True)
        return Response(serializer.data)
      stu = HotelImages.objects.all()
      serializer = RoomImagesSerializer(stu, many=True)
      return Response(serializer.data)


class roomImgaUpload(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request,  format=None):
        serializer = RoomImagesSerializer(data=request.data)
        if serializer.is_valid():
          serializer.save()
          return Response(serializer.data)
        return Response(serializer.errors)


class roomImgapiDelete(APIView):
    permission_classes = [IsAuthenticated]
    def delete(self, request, pk, format=None):
        id = pk
        stu = Room.objects.get(id=pk)
        stu.delete()
        return Response({'msg': 'deleted'})



def check_availability(room_no, checkin, checkout):
  avail_list = []
  check_in = datetime.datetime.strptime(checkin, '%Y-%m-%d %H:%M:%S.%f')
  check_out = datetime.datetime.strptime(checkout, '%Y-%m-%d %H:%M:%S.%f')
  booking_list = HotelBooking.objects.filter(room=room_no)
  for booking in booking_list:
    if booking.start_date > check_out or booking.end_date < check_in:
      avail_list.append(True)
    else:
      avail_list.append(False)
  return all(avail_list)



class hotelRoomBooking(APIView):
  # permission_classes = [IsAuthenticated]
  def post(self, request,  format=None):
    json_data = request.body
    stream = io.BytesIO(json_data)
    python_data = JSONParser().parse(stream)
    room = python_data.get('room')
    check_in = python_data.get('start_date')
    check_out = python_data.get('end_date')
    # check_availability(room, check_in, check_out)
    serializer = HotelBookingSerializer(data=request.data)
    if serializer.is_valid():
      if check_availability(room, check_in, check_out):
        serializer.save()
        return Response(serializer.data)
      return Response({'msg': 'this roon is booked on these date'})
    return Response(serializer.errors)



class bookdate(APIView):
    def get(self, request, pk=None, format=None):
      id = pk
      if id is not None:
        stu = HotelBooking.objects.filter(room=id)
        serializer = HotelBookingSerializer(stu, many=True)
        return Response(serializer.data)




class allroombookdate(APIView):
    def get(self, request, pk=None, format=None):
      id = pk
      if id is not None:
        stu = HotelBooking.objects.filter(hotel=id)
        serializer = HotelBookingSerializer(stu, many=True)
        return Response(serializer.data)