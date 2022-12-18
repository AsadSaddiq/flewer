from rest_framework import serializers
from hostels.models import Hostel
# from account.models import User
from hostels.models import Hostel, HostelBooking, HostelImages, RoomPhoto, Room, Rating


class HostelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hostel
        fields = ['id', 'user', 'hostel_photo', 'hostel_name', 'hostel_description', 'longitude', 'latitude', 'security_cameras', 'weapons', 'dangerous_animals']

class HostelgetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hostel
        fields = '__all__'

class HostelImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = HostelImages
        fields = '__all__'



class HostelBookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = HostelBooking
        fields = '__all__'


class HostelRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hostel
        fields = '__all__'


class RoomImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomPhoto
        fields = '__all__'



class RatingSerializer(serializers.ModelSerializer):
    # ratings = serializers.SerializerMethodField('get_ratings_detail')
    class Meta:
        model = Hostel
        fields = ['one', 'two', 'three', 'four', 'five']


class ratingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Rating
        fields = '__all__'
    