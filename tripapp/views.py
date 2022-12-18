from .models import TripComp, Trip, TripGuider, TripImages, CompRating, GuiRating, GuiderBooking, TripBooking
from .serializers import companySerializer, TripSerializer, GuiderSerializer, TripImagesSerializer, CompRatingSerializer, GuiRatingSerializer, compratingSerializer, guiratingSerializer, GuiderBookingSerializer, TripBookingSerializer, TripCompgetSerializer, GuidergetSerializer
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated 
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
import io
import datetime



class compcreate(APIView):
  permission_classes = [IsAuthenticated]
  def post(self, request,  format=None):
    serializer = companySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)


class compUpdate(APIView):
  permission_classes = [IsAuthenticated]
  def put(self, request, pk, format=None):
    id=pk
    stu = TripComp.objects.get(id=id)
    serializer = companySerializer(stu, data=request.data, partial=True)
    if serializer.is_valid():
     serializer.save()
     return Response(serializer.data)
    return Response(serializer.errors)


class compDestroy(APIView):
  permission_classes = [IsAuthenticated]
  def delete(self, request, pk, format=None):
    id = pk
    stu = TripComp.objects.get(id=pk)
    stu.delete()
    return Response({'msg': 'deleted'})


class compRetrieve(APIView):
  def get(self, request, pk=None, format=None):
    id = pk
    if id is not None:
      stu = TripComp.objects.filter(owner_id=id)
      serializer = companySerializer(stu, many=True)
      return Response(serializer.data)
    stu = TripComp.objects.all()
    serializer = companySerializer(stu, many=True)
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
    stu = TripComp.objects.get(id=id)
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

    serializer = CompRatingSerializer(stu, data=mylist, partial=True)
    if serializer.is_valid():
     serializer.save()
     return Response(serializer.data)
    return Response(serializer.errors)

class RatingCompany(APIView):
#   permission_classes = [IsAuthenticated]
  def get(self, request, pk=None, format=None):
    id = pk
    if id is not None:
      stu = TripComp.objects.filter(id=id)
      serializer = CompRatingSerializer(stu, many=True)
      return Response(serializer.data)
    # stu = Rating.objects.all()
    # serializer = RatingSerializer(stu, many=True)
    # return Response(serializer.data)









class companyRetrieve(APIView):
  def get(self, request, pk=None, format=None):
    id = pk
    if id is not None:
      stu = TripComp.objects.filter(id=id)
      serializer = companySerializer(stu, many=True)
      return Response(serializer.data)
    stu = TripComp.objects.all()
    serializer = companySerializer(stu, many=True)
    return Response(serializer.data)


# /////////////TRIP///////////////


class tripcreate(APIView):
  permission_classes = [IsAuthenticated]
  def post(self, request,  format=None):
    serializer = TripSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)


class tripUpdate(APIView):
  permission_classes = [IsAuthenticated]
  def put(self, request, pk, format=None):
    id=pk
    stu = Trip.objects.get(id=id)
    serializer = TripSerializer(stu, data=request.data, partial=True)
    if serializer.is_valid():
     serializer.save()
     return Response(serializer.data)
    return Response(serializer.errors)


class tripDestroy(APIView):
  permission_classes = [IsAuthenticated]
  def delete(self, request, pk, format=None):
    id = pk
    stu = Trip.objects.get(id=pk)
    stu.delete()
    return Response({'msg': 'deleted'})


class tripRetrieve(APIView):
  def get(self, request, pk=None, format=None):
    id = pk
    if id is not None:
      stu = Trip.objects.filter(trip_guider=id)
      serializer = TripSerializer(stu, many=True)
      return Response(serializer.data)
    stu = Trip.objects.all()
    serializer = TripSerializer(stu, many=True)
    return Response(serializer.data)

# /////////////TRIP IMAGES//////////////



class tripImagescreate(APIView):
  permission_classes = [IsAuthenticated]
  def post(self, request,  format=None):
    serializer = TripImagesSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)


class tripImagesUpdate(APIView):
  permission_classes = [IsAuthenticated]
  def put(self, request, pk, format=None):
    id=pk
    stu = TripImages.objects.get(id=id)
    serializer = TripImagesSerializer(stu, data=request.data, partial=True)
    if serializer.is_valid():
     serializer.save()
     return Response(serializer.data)
    return Response(serializer.errors)


class tripImagesDestroy(APIView):
  permission_classes = [IsAuthenticated]
  def delete(self, request, pk, format=None):
    id = pk
    stu = TripImages.objects.get(id=pk)
    stu.delete()
    return Response({'msg': 'deleted'})


class tripImagesRetrieve(APIView):
  def get(self, request, pk=None, format=None):
    id = pk
    if id is not None:
      stu = TripImages.objects.filter(place=id)
      serializer = TripImagesSerializer(stu, many=True)
      return Response(serializer.data)
    stu = TripImages.objects.all()
    serializer = TripImagesSerializer(stu, many=True)
    return Response(serializer.data)




class tripguidercreate(APIView):
  permission_classes = [IsAuthenticated]
  def post(self, request,  format=None):
    serializer = GuiderSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)


class tripguiderUpdate(APIView):
  permission_classes = [IsAuthenticated]
  def put(self, request, pk, format=None):
    id=pk
    stu = TripGuider.objects.get(id=id)
    serializer = GuiderSerializer(stu, data=request.data, partial=True)
    if serializer.is_valid():
     serializer.save()
     return Response(serializer.data)
    return Response(serializer.errors)


class tripguiderDestroy(APIView):
  permission_classes = [IsAuthenticated]
  def delete(self, request, pk, format=None):
    id = pk
    stu = TripGuider.objects.get(id=pk)
    stu.delete()
    return Response({'msg': 'deleted'})


class tripguiderRetrieve(APIView):
  def get(self, request, pk=None, format=None):
    id = pk
    if id is not None:
      stu = TripGuider.objects.filter(trip_comp=id)
      serializer = GuiderSerializer(stu, many=True)
      return Response(serializer.data)
    stu = TripGuider.objects.all()
    serializer = GuiderSerializer(stu, many=True)
    return Response(serializer.data)



class GuiderRatingUpdate(APIView):
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
    stu = TripGuider.objects.get(id=id)
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

    serializer = GuiRatingSerializer(stu, data=mylist, partial=True)
    if serializer.is_valid():
     serializer.save()
     return Response(serializer.data)
    return Response(serializer.errors)

class RatingGuider(APIView):
#   permission_classes = [IsAuthenticated]
  def get(self, request, pk=None, format=None):
    id = pk
    if id is not None:
      stu = TripGuider.objects.filter(id=id)
      serializer = GuiRatingSerializer(stu, many=True)
      return Response(serializer.data)
    

# /////////////////////  REVIEW  ///////////////////////////////

class CompRatcreate(APIView):
  def post(self, request,  format=None):
    serializer = compratingSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)


class CompRatRetrieve(APIView):
#   permission_classes = [IsAuthenticated]
  def get(self, request, pk=None, format=None):
    id = pk
    if id is not None:
      stu = CompRating.objects.filter(comp=id)
      serializer = compratingSerializer(stu, many=True)
      return Response(serializer.data)
    stu = CompRating.objects.all()
    serializer = compratingSerializer(stu, many=True)
    return Response(serializer.data)


# /////////////////////  REVIEW  ///////////////////////////////

class GuiRatcreate(APIView):
  def post(self, request,  format=None):
    serializer = guiratingSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)


class GuiRatRetrieve(APIView):
#   permission_classes = [IsAuthenticated]
  def get(self, request, pk=None, format=None):
    id = pk
    if id is not None:
      stu = GuiRating.objects.filter(guid=id)
      serializer = guiratingSerializer(stu, many=True)
      return Response(serializer.data)
    stu = GuiRating.objects.all()
    serializer = guiratingSerializer(stu, many=True)
    return Response(serializer.data)




class bookdate(APIView):
    def get(self, request, pk, format=None):
      id = pk
      if id is not None:
        stu = GuiderBooking.objects.filter(guider=id)
        serializer = GuiderBookingSerializer(stu, many=True)
        return Response(serializer.data)
      




def check_availability(guider_id, checkin, checkout):
  avail_list = []
  check_in = datetime.datetime.strptime(checkin, '%Y-%m-%d %H:%M:%S.%f')
  check_out = datetime.datetime.strptime(checkout, '%Y-%m-%d %H:%M:%S.%f')
  booking_list = GuiderBooking.objects.filter(guider=guider_id)
  for booking in booking_list:
    if booking.start_date > check_out or booking.end_date < check_in:
      avail_list.append(True)
    else:
      avail_list.append(False)
  return all(avail_list)



class tripGuiderBooking(APIView):
  # permission_classes = [IsAuthenticated]
  def post(self, request,  format=None):
    json_data = request.body
    stream = io.BytesIO(json_data)
    python_data = JSONParser().parse(stream)
    guider = python_data.get('guider')
    check_in = python_data.get('start_date')
    check_out = python_data.get('end_date')
    # check_availability(room, check_in, check_out)
    serializer = GuiderBookingSerializer(data=request.data)
    if serializer.is_valid():
      if check_availability(guider, check_in, check_out):
        serializer.save()
        return Response(serializer.data)
      return Response({'msg': 'this roon is booked on these date'})
    return Response(serializer.errors)




class comptripbooking(APIView):
  permission_classes = [IsAuthenticated]
  def post(self, request,  format=None):
    serializer = TripBookingSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)


class tripbookdate(APIView):
    def get(self, request, pk, format=None):
      id = pk
      if id is not None:
        stu = TripBooking.objects.filter(trip=id)
        serializer = TripBookingSerializer(stu, many=True)
        return Response(serializer.data)
      


class favCompRetrieve(APIView):
#   permission_classes = [IsAuthenticated]
  def get(self, request, pk=None, format=None):
    id = pk
    if id is not None:
      stu = TripComp.objects.filter(id=id)
      serializer = TripCompgetSerializer(stu, many=True)
      return Response(serializer.data)


class favGuiderRetrieve(APIView):
#   permission_classes = [IsAuthenticated]
  def get(self, request, pk=None, format=None):
    id = pk
    if id is not None:
      stu = TripGuider.objects.filter(id=id)
      serializer = GuidergetSerializer(stu, many=True)
      return Response(serializer.data)