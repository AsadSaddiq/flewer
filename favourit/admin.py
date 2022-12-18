from django.contrib import admin
from favourit.models import FavouritHostel, FavouritHotel, FavouritHouse, FavouritTripComp, FavouritGuider
from payment.models import PaymentHistory

# Register your models here.

class favTripComp(admin.ModelAdmin):
    class Meta:
        model = FavouritTripComp
admin.site.register(FavouritTripComp, favTripComp)


class favGuider(admin.ModelAdmin):
    class Meta:
        model = FavouritGuider
admin.site.register(FavouritGuider, favGuider)




class favHostel(admin.ModelAdmin):
    class Meta:
        model = FavouritHostel
admin.site.register(FavouritHostel, favHostel)




class favHouse(admin.ModelAdmin):
    class Meta:
        model = FavouritHouse
admin.site.register(FavouritHouse, favHouse)