from rest_framework import serializers
from .models import FavouritHostel, FavouritHotel, FavouritHouse, FavouritGuider, FavouritTripComp



class FavHotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = FavouritHotel
        fields = '__all__'


class FavHostelSerializer(serializers.ModelSerializer):
    class Meta:
        model = FavouritHostel
        fields = '__all__'

class FavHouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = FavouritHouse
        fields = '__all__'

class FavTripCompSerializer(serializers.ModelSerializer):
    class Meta:
        model = FavouritTripComp
        fields = '__all__'

class FavGuiderSerializer(serializers.ModelSerializer):
    class Meta:
        model = FavouritGuider
        fields = '__all__'


