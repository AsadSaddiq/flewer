from ast import Or
from django.http.response import JsonResponse
# from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from chat.models import Contact, Message
from chat.serializers import MessageSerializer, contentListSerializer, ContactSerializer, ContactRetrieveSerializer
from rest_framework.views import APIView
from accounts.models import UserAccount
from accounts.serializers import UserCreateSerializer
from rest_framework.response import Response
from django.shortcuts import render


class user_list(APIView):
#   permission_classes = [IsAuthenticated]
  def get(self, request, pk=None, format=None):
    id = pk
    if id is not None:
      stu = UserAccount.objects.filter(id=id)
      serializer = UserCreateSerializer(stu, many=True)
      return Response(serializer.data)
    stu = UserAccount.objects.all()
    serializer = UserCreateSerializer(stu, many=True)
    return Response(serializer.data)


class message(APIView):
    def get(self, request, sender=None, receiver=None):
      messages = Message.objects.filter(sender=sender, receiver=receiver) | Message.objects.filter(sender=receiver, receiver=sender)
      print(messages)
      serializer = MessageSerializer(messages, many=True, context={'request': request})
      for message in messages:
            message.is_read = True
            message.save()
      return Response(serializer.data)

class message_list(APIView):
    def post(self, request,  format=None):
        serializer = MessageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)



class contact_list(APIView):
    def get(self, request, pk=None):
      id=pk
   
      messages = Message.objects.filter(receiver=id) 
      serializer = contentListSerializer(messages, many=True, context={'request': request})
      # serializer2 = contentListSerializer(messages2, many=True, context={'request': request})
      return JsonResponse(serializer.data, safe=False)
      

class ContactList(APIView):
    def post(self, request,  format=None):
        serializer = ContactSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


class contact_retrieve(APIView):
    def get(self, request, sender=None):
      id = sender
      contact = Contact.objects.filter(receiver_id=id) | Contact.objects.filter(sender_id=id) 
      serializer = ContactRetrieveSerializer(contact, many=True)
      return Response(serializer.data)