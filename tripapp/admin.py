from django.contrib import admin
from tripapp.models import GuiderBooking, TripComp, TripGuider, Trip, TripImages, CompRating, GuiRating, TripBooking



class TripCompany(admin.ModelAdmin):
    list_display = ('id', 'com_name', 'com_img', 'owner_name', 'about_comp')
admin.site.register(TripComp, TripCompany)


class Trip_Guider(admin.ModelAdmin):
    list_display = ('id', 'name', 'image', 'about', 'location', 'latitude', 'longitude', 'price')
admin.site.register(TripGuider, Trip_Guider)

class GuiderBookingAdmin(admin.ModelAdmin):
    class Meta:
        model = GuiderBooking
admin.site.register(GuiderBooking, GuiderBookingAdmin)

class TripBookingAdmin(admin.ModelAdmin):
    class Meta:
        model = TripBooking
admin.site.register(TripBooking, TripBookingAdmin)

class TripRoot(admin.ModelAdmin):
    list_display = ('id','trip_name', 'start_date', 'end_date', 'duration', 'location', 'latitude', 'longitude', 'vistingPlaces', 'c_type', 'single_price', 'cuple_price')
admin.site.register(Trip, TripRoot)

class TripImag(admin.ModelAdmin):
    list_display = ('id', 'title', 'image')
admin.site.register(TripImages, TripImag)


class CompanyRatingAdmin(admin.ModelAdmin):
    list_display = ('comp', 'name', 'one', 'two', 'three', 'four', 'five', 'review')
admin.site.register(CompRating, CompanyRatingAdmin)

class GuiderRatingAdmin(admin.ModelAdmin):
    list_display = ('guid', 'name', 'one', 'two', 'three', 'four', 'five', 'review')
admin.site.register(GuiRating, GuiderRatingAdmin)