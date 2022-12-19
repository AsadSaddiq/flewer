from .models import Hostel, HostelBooking, HostelImages, Room, RoomPhoto, Rating
from .serializers import HostelSerializer, HostelImagesSerializer, RoomImagesSerializer, HostelBookingSerializer, HostelRoomSerializer, RatingSerializer, ratingSerializer, HostelgetSerializer
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
import datetime
from rest_framework.parsers import JSONParser
import io



class hostelcreate(APIView):
#   renderer_classes = [UserRenderer]
  permission_classes = [IsAuthenticated]
  def post(self, request,  format=None):
    serializer = HostelSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)


class hostelUpdate(APIView):
#   renderer_classes = [UserRenderer]
  permission_classes = [IsAuthenticated]
  def put(self, request, pk, format=None):
    id=pk
    stu = Hostel.objects.get(id=id)
    serializer = HostelSerializer(stu, data=request.data, partial=True)
    if serializer.is_valid():
     serializer.save()
     return Response(serializer.data)
    return Response(serializer.errors)


class hostelDestroy(APIView):
  permission_classes = [IsAuthenticated]
  def delete(self, request, pk, format=None):
    id = pk
    stu = Hostel.objects.get(id=pk)
    stu.delete()
    return Response({'msg': 'deleted'})


class hostelRetrieve(APIView):
#   permission_classes = [IsAuthenticated]
  def get(self, request, pk=None, format=None):
    id = pk
    if id is not None:
        stu = Hostel.objects.filter(user=id)
        serializer = HostelgetSerializer(stu, many=True)
        return Response(serializer.data)
    stu = Hostel.objects.all()
    serializer = HostelgetSerializer(stu, many=True)
    return Response(serializer.data)


class favhostelRetrieve(APIView):
#   permission_classes = [IsAuthenticated]
  def get(self, request, pk=None, format=None):
    id = pk
    if id is not None:
      stu = Hostel.objects.filter(id=id)
      serializer = HostelgetSerializer(stu, many=True)
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
    stu = Hostel.objects.get(id=id)
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

    serializer = RatingSerializer(stu, data=mylist, partial=True)
    if serializer.is_valid():
     serializer.save()
     return Response(serializer.data)
    return Response(serializer.errors)

class RatingHostel(APIView):
#   permission_classes = [IsAuthenticated]
  def get(self, request, pk=None, format=None):
    id = pk
    if id is not None:
      stu = Hostel.objects.filter(id=id)
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
      stu = Rating.objects.filter(hostel=id)
      serializer = ratingSerializer(stu, many=True)
      return Response(serializer.data)
    stu = Rating.objects.all()
    serializer = ratingSerializer(stu, many=True)
    return Response(serializer.data)




class hostelImgapi(APIView):
    # permission_classes = [IsAuthenticated]
    def get(self, request, pk=None, format=None):
      id = pk
      if id is not None:
        stu = HostelImages.objects.filter(hostel=id)
        serializer = HostelImagesSerializer(stu, many=True)
        return Response(serializer.data)
      stu = HostelImages.objects.all()
      serializer = HostelImagesSerializer(stu, many=True)
      return Response(serializer.data)


class hostelImgaUpload(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request,  format=None):
        serializer = HostelImagesSerializer(data=request.data)
        if serializer.is_valid():
          serializer.save()
          return Response(serializer.data)
        return Response(serializer.errors)


class hostelImgapiDelete(APIView):
    permission_classes = [IsAuthenticated]
    def delete(self, request, pk, format=None):
        id = pk
        stu = Hostel.objects.get(id=pk)
        stu.delete()
        return Response({'msg': 'deleted'})




class RoomCreate(APIView):
#   renderer_classes = [UserRenderer]
  permission_classes = [IsAuthenticated]
  def post(self, request,  format=None):
    serializer = HostelRoomSerializer(data=request.data)
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
    serializer = HostelRoomSerializer(stu, data=request.data, partial=True)
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
        stu = Room.objects.filter(hostel=id)
        serializer = HostelRoomSerializer(stu, many=True)
        return Response(serializer.data)
    stu = Room.objects.all()
    serializer = HostelRoomSerializer(stu, many=True)
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





# obj = Hostel.objects.get(id=1)
# field_object = Hostel._meta.get_field('avaliable_gust_seat')
# field_value = getattr(obj, field_object.attname)
# print(field_value)

class hostelRoomBooking(APIView):
  # permission_classes = [IsAuthenticated]
  def post(self, request,  format=None):
    json_data = request.body
    stream = io.BytesIO(json_data)
    python_data = JSONParser().parse(stream)
    gust = python_data.get('no_gust')
    pk = python_data.get('hostel')

    obj = Hostel.objects.get(id=pk)
    field_object = Hostel._meta.get_field('avaliable_gust_seat')
    field_value = getattr(obj, field_object.attname)
    print(field_value)
    if gust < field_value:
     serializer = HostelBookingSerializer(data=request.data)
     if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response({'msg': 'this hostel is booked on these date'})
    # return Response(serializer.errors)



class bookdate(APIView):
    def get(self, request, pk=None, format=None):
      id = pk
      if id is not None:
        stu = HostelBooking.objects.filter(room=id)
        serializer = HostelBookingSerializer(stu, many=True)
        return Response(serializer.data)



class allroombookdate(APIView):
    def get(self, request, pk=None, format=None):
      id = pk
      if id is not None:
        stu = HostelBooking.objects.filter(hostel=id)
        serializer = HostelBookingSerializer(stu, many=True)
        return Response(serializer.data)