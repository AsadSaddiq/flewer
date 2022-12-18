from .models import PaymentHistory
from .serializers import P_historySerializer
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response



class S_History(APIView):
  permission_classes = [IsAuthenticated]
  def get(self, request, pk=None, format=None):
    id = pk
    if id is not None:
      stu = PaymentHistory.objects.filter(superuser=id)
      serializer = P_historySerializer(stu, many=True)
      return Response(serializer.data)




class O_History(APIView):
  permission_classes = [IsAuthenticated]
  def get(self, request, pk=None, format=None):
    id = pk
    if id is not None:
      stu = PaymentHistory.objects.filter(owner_id=id)
      serializer = P_historySerializer(stu, many=True)
      return Response(serializer.data)



class B_History(APIView):
  permission_classes = [IsAuthenticated]
  def get(self, request, pk=None, format=None):
    id = pk
    if id is not None:
      stu = PaymentHistory.objects.filter(booker_id=id)
      serializer = P_historySerializer(stu, many=True)
      return Response(serializer.data)




class historycreate(APIView):
#   renderer_classes = [UserRenderer]
  permission_classes = [IsAuthenticated]
  def post(self, request,  format=None):
    serializer = P_historySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)