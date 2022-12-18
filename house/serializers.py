from rest_framework import serializers
from house.models import House, HouseBooking, HouseImages, Rating, Room, RoomPhoto
from accounts.models import UserAccount


class HouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = House
        fields = ['id', 'house', 'house_name', 'description', 'longitude', 'latitude', 'guests', 'bed_count', 'room_count', 'bathroom_count', 'security_cameras', 'weapons', 'dangerous_animals', 'c_type', 'house_price', 'is_apartment', 'free_wifi', 'refrigerator', 'telephone', 'ironing_facilities', 'wake_up_service', 'electric_kettle', 'tea_coffee_maker', 'daily_housekeeping', 'city_view']
        

class HousegetSerializer(serializers.ModelSerializer):
    class Meta:
        model = House
        fields = '__all__'


class RatingSerializer(serializers.ModelSerializer):
    # ratings = serializers.SerializerMethodField('get_ratings_detail')
    class Meta:
        model = House
        fields = ['one', 'two', 'three', 'four', 'five']



class ratingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Rating
        fields = '__all__'
    

class HouseImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = HouseImages
        fields = '__all__'


class HouseRoomSerializer(serializers.ModelSerializer):
    # room_Name = serializers.CharField(max_length=100)
    class Meta:
        model = Room
        fields = '__all__'

class RoomImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomPhoto
        fields = '__all__'



class HouseBookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = HouseBooking
        fields = '__all__'
        

