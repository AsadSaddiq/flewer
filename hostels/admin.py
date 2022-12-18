from django.contrib import admin
from .models import *



class HostelAdmin(admin.ModelAdmin):
    list_display = ('id', 'hostel_name', 'hostel_description','longitude', 'latitude', 'created_at', 'updated_at', 'security_cameras', 'weapons', 'dangerous_animals')
admin.site.register(Hostel, HostelAdmin)


class HostelImagesAdmin(admin.ModelAdmin):
    list_display = ('hostel', 'images')
admin.site.register(HostelImages, HostelImagesAdmin)


class RatingAdmin(admin.ModelAdmin):
    list_display = ('hostel', 'name', 'one', 'two', 'three', 'four', 'five', 'review')
admin.site.register(Rating, RatingAdmin)


class RoomAdmin(admin.ModelAdmin):
    class Meta:
        model = Room
admin.site.register(Room, RoomAdmin)


class RoomImagesAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'image', 'room')
admin.site.register(RoomPhoto, RoomImagesAdmin)



class HostelBookingAdmin(admin.ModelAdmin):
    list_display = ('hostel', 'no_gust', 'hostel_name',  'user', 'client_name', 'hostel', 'start_date', 'end_date', 'c_type', 'prics')
admin.site.register(HostelBooking, HostelBookingAdmin)
