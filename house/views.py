from .models import HouseBooking, HouseImages, House, Rating, Room, RoomPhoto
from .serializers import HouseSerializer, HouseImagesSerializer, HouseRoomSerializer, RoomImagesSerializer, HouseBookingSerializer, RatingSerializer, ratingSerializer, HousegetSerializer
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated 
from rest_framework.response import Response
import datetime
from rest_framework.parsers import JSONParser
import io


class housecreate(APIView):
#   renderer_classes = [UserRenderer]
  permission_classes = [IsAuthenticated]
  def post(self, request,  format=None):
    serializer = HouseSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)


class houseUpdate(APIView):
  permission_classes = [IsAuthenticated]
  def put(self, request, pk, format=None):
    id=pk
    stu = House.objects.get(id=id)
    serializer = HouseSerializer(stu, data=request.data, partial=True)
    if serializer.is_valid():
     serializer.save()
     return Response(serializer.data)
    return Response(serializer.errors)


class houseDestroy(APIView):
  permission_classes = [IsAuthenticated]
  def delete(self, request, pk, format=None):
    id = pk
    stu = House.objects.get(id=pk)
    stu.delete()
    return Response({'msg': 'deleted'})


class houseRetrieve(APIView):
#   permission_classes = [IsAuthenticated]
  def get(self, request, pk=None, format=None):
    id = pk
    if id is not None:
      stu = House.objects.filter(house=id)
      serializer = HousegetSerializer(stu, many=True)
      return Response(serializer.data)
    stu = House.objects.all()
    serializer = HousegetSerializer(stu, many=True)
    return Response(serializer.data)


class favhouseRetrieve(APIView):
#   permission_classes = [IsAuthenticated]
  def get(self, request, pk=None, format=None):
    id = pk
    if id is not None:
      stu = House.objects.filter(id=id)
      serializer = HousegetSerializer(stu, many=True)
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
    print(onestar)
    id=pk
    stu = House.objects.get(id=id)
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

class RatingHouse(APIView):
#   permission_classes = [IsAuthenticated]
  def get(self, request, pk=None, format=None):
    id = pk
    if id is not None:
      stu = House.objects.filter(id=id)
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
      stu = Rating.objects.filter(house=id)
      serializer = ratingSerializer(stu, many=True)
      return Response(serializer.data)
    stu = Rating.objects.all()
    serializer = ratingSerializer(stu, many=True)
    return Response(serializer.data)








class houseImgapi(APIView):
  def get(self, request, pk=None, format=None):
    id = pk
    if id is not None:
      stu = HouseImages.objects.filter(house=id)
      serializer = HouseImagesSerializer(stu, many=True)
      return Response(serializer.data)
    stu = HouseImages.objects.all()
    serializer = HouseImagesSerializer(stu, many=True)
    return Response(serializer.data)

class houseImgaUpload(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request,  format=None):
        serializer = HouseImagesSerializer(data=request.data)
        if serializer.is_valid():
          serializer.save()
          return Response(serializer.data)
        return Response(serializer.errors)


class houseImgapiDelete(APIView):
    permission_classes = [IsAuthenticated]
    def delete(self, request, pk, format=None):
        id = pk
        stu = House.objects.get(id=pk)
        stu.delete()
        return Response({'msg': 'deleted'})




class RoomCreate(APIView):
  permission_classes = [IsAuthenticated]
  def post(self, request,  format=None):
    serializer = HouseRoomSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)




class RoomUpdate(APIView):
  permission_classes = [IsAuthenticated]
  def put(self, request, pk, format=None):
    id=pk
    stu = Room.objects.get(id=id)
    serializer = HouseRoomSerializer(stu, data=request.data, partial=True)
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
        stu = Room.objects.filter(house=id)
        serializer = HouseRoomSerializer(stu, many=True)
        return Response(serializer.data)
    stu = Room.objects.all()
    serializer = HouseRoomSerializer(stu, many=True)
    return Response(serializer.data)

# ROOM IMAGES FUNCTIONS/////////////////////////////////////////////////////////

class roomImgapi(APIView):
    def get(self, request, pk=None, format=None):
      id = pk
      if id is not None:
        stu = RoomPhoto.objects.filter(room=id)
        serializer = RoomImagesSerializer(stu, many=True)
        return Response(serializer.data)
      stu = RoomPhoto.objects.all()
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



def check_availability(house, checkin, checkout):
  avail_list = []
  check_in = datetime.datetime.strptime(checkin, '%Y-%m-%d %H:%M:%S.%f')
  check_out = datetime.datetime.strptime(checkout, '%Y-%m-%d %H:%M:%S.%f')
  booking_list = HouseBooking.objects.filter(house=house)
  for booking in booking_list:
    if booking.start_date > check_out or booking.end_date < check_in:
      avail_list.append(True)
    else:
      avail_list.append(False)
  return all(avail_list)



class houseBooking(APIView):
  # permission_classes = [IsAuthenticated]
  def post(self, request,  format=None):
    json_data = request.body
    stream = io.BytesIO(json_data)
    python_data = JSONParser().parse(stream)
    house = python_data.get('house')
    check_in = python_data.get('start_date')
    check_out = python_data.get('end_date')
    serializer = HouseBookingSerializer(data=request.data)
    if serializer.is_valid():
      if check_availability(house, check_in, check_out):
        serializer.save()
        return Response(serializer.data)
      return Response({'msg': 'this house is booked on these date'})
    return Response(serializer.errors)


class bookdate(APIView):
    def get(self, request, pk=None, format=None):
      id = pk
      if id is not None:
        stu = HouseBooking.objects.filter(house=id)
        serializer = HouseBookingSerializer(stu, many=True)
        return Response(serializer.data)
      

  
class allroombookdate(APIView):
    def get(self, request, pk=None, format=None):
      id = pk
      if id is not None:
        stu = HouseBooking.objects.filter(house=id)
        serializer = HouseBookingSerializer(stu, many=True)
        return Response(serializer.data)
