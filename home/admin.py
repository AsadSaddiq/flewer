from django.contrib import admin
from .models import *



class HotelAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'hotel_name', 'hotel_description', 'longitude', 'latitude', 'created_at', 'updated_at', 'security_cameras', 'weapons', 'dangerous_animals')
admin.site.register(Hotel, HotelAdmin)


class HotelImagesAdmin(admin.ModelAdmin):
    list_display = ('id', 'hotel', 'image')
admin.site.register(HotelImages, HotelImagesAdmin)


class RoomAdmin(admin.ModelAdmin):
    class Meta:
        model = Room
admin.site.register(Room, RoomAdmin)


class RatingAdmin(admin.ModelAdmin):
    list_display = ('hotel', 'name', 'one', 'two', 'three', 'four', 'five', 'review')
admin.site.register(Rating, RatingAdmin)


class RoomImagesAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'image', 'room')
admin.site.register(RoomPhoto, RoomImagesAdmin)




class HotelBookingAdmin(admin.ModelAdmin):
    list_display = ('room', 'room_name', 'hotel_name',  'user', 'client_name', 'hotel', 'start_date', 'end_date', 'c_type', 'price')
admin.site.register(HotelBooking, HotelBookingAdmin)
