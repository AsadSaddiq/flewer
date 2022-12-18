from django.contrib import admin
from .models import *



class HouseAdmin(admin.ModelAdmin):
    list_display = ('house_name', 'house_price', 'created_at', 'description', 'room_count')
admin.site.register(House, HouseAdmin)


class HouseImagesAdmin(admin.ModelAdmin):
    list_display = ('house', 'images')
admin.site.register(HouseImages, HouseImagesAdmin)



class RoomAdmin(admin.ModelAdmin):
    class Meta:
        model = Room
admin.site.register(Room, RoomAdmin)


class RoomImagesAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'image', 'room')
admin.site.register(RoomPhoto, RoomImagesAdmin)


class HouseBookingAdmin(admin.ModelAdmin):
    list_display = ('house_name',  'user', 'client_name', 'house', 'start_date', 'end_date', 'c_type', 'prics')
admin.site.register(HouseBooking, HouseBookingAdmin)


class RatingAdmin(admin.ModelAdmin):
    list_display = ('house', 'name', 'one', 'two', 'three', 'four', 'five', 'review')
admin.site.register(Rating, RatingAdmin)
