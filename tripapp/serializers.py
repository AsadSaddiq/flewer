from rest_framework import serializers
from .models import TripComp, Trip, TripGuider, TripImages, CompRating, GuiRating, TripBooking, GuiderBooking


class companySerializer(serializers.ModelSerializer):
    class Meta:
        model = TripComp
        fields = '__all__'

class TripCompgetSerializer(serializers.ModelSerializer):
    # hotel_name = serializers.CharField(max_length=100)
    class Meta:
        model = TripComp
        fields = '__all__'


class GuidergetSerializer(serializers.ModelSerializer):
    # hotel_name = serializers.CharField(max_length=100)
    class Meta:
        model = TripGuider
        fields = '__all__'

class TripSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trip
        fields = '__all__'


class CompRatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = TripComp
        fields = ['one', 'two', 'three', 'four', 'five']

class TripImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = TripImages
        fields = '__all__'

class GuiderSerializer(serializers.ModelSerializer):
    class Meta:
        model = TripGuider
        fields = '__all__'


class GuiRatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = TripGuider
        fields = ['one', 'two', 'three', 'four', 'five']



class compratingSerializer(serializers.ModelSerializer):

    class Meta:
        model = CompRating
        fields = '__all__'
    

class guiratingSerializer(serializers.ModelSerializer):

    class Meta:
        model = GuiRating
        fields = '__all__'
    
class TripBookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = TripBooking
        fields = '__all__'


class GuiderBookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = GuiderBooking
        fields = '__all__'