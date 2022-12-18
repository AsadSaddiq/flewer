# from django.contrib.auth.models import User
from rest_framework import serializers
from chat.models import Contact, Message
from accounts.models import UserAccount




class MessageSerializer(serializers.ModelSerializer):
    # sender = serializers.SlugRelatedField(many=False, slug_field='first_name', queryset=User.objects.all())
    # receiver = serializers.SlugRelatedField(many=False, slug_field='first_name', queryset=User.objects.all())

    class Meta:
        model = Message
        fields = ['sender', 'receiver', 'message', 'timestamp']



class contentListSerializer(serializers.ModelSerializer):
    sender = serializers.SlugRelatedField(many=False, slug_field='first_name', queryset=UserAccount.objects.all())
    receiver = serializers.SlugRelatedField(many=False, slug_field='first_name', queryset=UserAccount.objects.all())

    class Meta:
        model = Message
        fields = ['sender', 'receiver', 'message', 'timestamp']


class ContactSerializer(serializers.ModelSerializer):
    # sender_name = serializers.SlugRelatedField(many=False, slug_field='first_name', queryset=User.objects.all())
    # receiver_name = serializers.SlugRelatedField(many=False, slug_field='first_name', queryset=User.objects.all())
    

    class Meta:
        model = Contact
        fields = ['id', 'sender_id', 'receiver_id', 'img', 'sender_name', 'receiver_name']


class ContactRetrieveSerializer(serializers.ModelSerializer):
    sender_name = serializers.SlugRelatedField(many=False, slug_field='first_name', queryset=UserAccount.objects.all())
    receiver_name = serializers.SlugRelatedField(many=False, slug_field='first_name', queryset=UserAccount.objects.all())
    

    class Meta:
        model = Contact
        fields = ['id', 'sender_id', 'receiver_id', 'img', 'sender_name', 'receiver_name']