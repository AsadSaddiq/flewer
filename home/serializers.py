from rest_framework import serializers
from home.models import Hotel, HotelBooking, HotelImages, Room, RoomPhoto, Rating

class HotelImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = HotelImages
        fields = '__all__'


class HotelSerializer(serializers.ModelSerializer):
    hotel_name = serializers.CharField(max_length=100)
    class Meta:
        model = Hotel
        fields = ['id', 'user', 'hotel_name', 'hotel_description', 'longitude', 'latitude', 'security_cameras', 'weapons', 'dangerous_animals']

class HotelgetSerializer(serializers.ModelSerializer):
    # hotel_name = serializers.CharField(max_length=100)
    class Meta:
        model = Hotel
        fields = '__all__'


class HotelRoomSerializer(serializers.ModelSerializer):
    # room_Name = serializers.CharField(max_length=100)
    class Meta:
        model = Room
        fields = '__all__'

class RoomImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomPhoto
        fields = '__all__'




class HotelBookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = HotelBooking
        fields = '__all__'


class RatingSerializer(serializers.ModelSerializer):
    # ratings = serializers.SerializerMethodField('get_ratings_detail')
    class Meta:
        model = Hotel
        fields = ['one', 'two', 'three', 'four', 'five']


class ratingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Rating
        fields = '__all__'
    