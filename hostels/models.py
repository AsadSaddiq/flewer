
from http import client
# from django.contrib.auth.models import User
from django.db import models
from accounts.models import UserAccount
import uuid

class HostelsModel(models.Model):
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now_add=True)

    class Meta:
        abstract = True




class Hostel(HostelsModel):
    user= models.ForeignKey(UserAccount ,related_name="HostelModel", on_delete=models.CASCADE)
    hostel_photo = models.ImageField(default='default.jpg', upload_to='room_photos')
    hostel_name= models.CharField(max_length=100)
    gender= models.CharField(max_length=100)
    no_gust= models.IntegerField()
    avaliable_gust_seat= models.IntegerField()
    hostel_description = models.TextField()
    location= models.CharField(max_length=100)
    longitude= models.CharField(max_length=100)
    latitude= models.CharField(max_length=100)
    security_cameras=models.BooleanField()
    weapons=models.BooleanField()
    dangerous_animals=models.BooleanField()
    one = models.PositiveIntegerField(default=0, null=True, blank=True)
    two = models.PositiveIntegerField(default=0, null=True, blank=True)
    three = models.PositiveIntegerField(default=0, null=True, blank=True)
    four = models.PositiveIntegerField(default=0, null=True, blank=True)
    five = models.PositiveIntegerField(default=0, null=True, blank=True)


    def __str__(self) -> str:
        return self.hostel_name



class HostelImages(HostelsModel):
    hostel= models.ForeignKey(Hostel , on_delete=models.CASCADE)
    images = models.ImageField(upload_to="hostel")



class Room(models.Model):
    """Creates room details"""

    hostel = models.ForeignKey(Hostel, on_delete=models.CASCADE )
    room_photo = models.ImageField(default='default.jpg', upload_to='room_photos')
    room_Name = models.CharField(max_length=200)
    room_details = models.CharField(max_length=500)
    max_adults = models.PositiveIntegerField(default=1)
    max_child = models.PositiveIntegerField(default=1)
    beds_count = models.PositiveIntegerField(default=0)
    extra_beds = models.PositiveIntegerField(default=0)
    C_type = models.CharField(max_length=200)
    extra_bed_price = models.PositiveIntegerField(default=1)
    room_Price = models.PositiveIntegerField(default=1)
    total_Rooms = models.PositiveIntegerField(default=1)  # room quantity
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    is_conference_room = models.BooleanField(default=False)
    is_apartment = models.BooleanField(default=False)
    # /////////Room ammenities////////////////////////////////
    free_toiletries = models.BooleanField(default=False)
    water_body_view = models.BooleanField(default=False)
    safe_deposit_box = models.BooleanField(default=False)
    lcd_tv = models.BooleanField(default=False)
    free_wifi = models.BooleanField(default=False)
    pay_tv = models.BooleanField(default=False)
    mini_bar = models.BooleanField(default=False)
    refrigerator = models.BooleanField(default=False)
    blackout_drapes = models.BooleanField(default=False)
    telephone = models.BooleanField(default=False)
    ironing_facilities = models.BooleanField(default=False)
    desk = models.BooleanField(default=False)
    hair_dryer = models.BooleanField(default=False)
    extra_towels = models.BooleanField(default=False)
    bathrobes = models.BooleanField(default=False)
    wake_up_service = models.BooleanField(default=False)
    electric_kettle = models.BooleanField(default=False)
    warddrobe = models.BooleanField(default=False)
    toilet_paper = models.BooleanField(default=False)
    slippers = models.BooleanField(default=False)
    toilet = models.BooleanField(default=False)
    alarm_clock = models.BooleanField(default=False)
    tea_coffee_maker = models.BooleanField(default=False)
    bathtub_shower = models.BooleanField(default=False)
    makeup_shaving_mirror = models.BooleanField(default=False)
    city_view = models.BooleanField(default=False)
    air_conditioner = models.BooleanField(default=False)
    cribs_infant_beds = models.BooleanField(default=False)
    daily_housekeeping = models.BooleanField(default=False)
    garden_view = models.BooleanField(default=False)
    #////// conference room ammenities///////////////////////////
    projector = models.BooleanField(default=False)
    screen = models.BooleanField(default=False)
    conference_phone = models.BooleanField(default=False)
    water = models.BooleanField(default=False)
    speakers = models.BooleanField(default=False)
    whiteboard = models.BooleanField(default=False)
    sockets = models.BooleanField(default=False)
    coffee = models.BooleanField(default=False)
    monitors = models.BooleanField(default=False)

    class Meta:
        ordering = ['room_Price', 'updated_at', ]

    def __str__(self):
        return f'({self.room_Name})'

    def save(self, *args, **kwargs):
        """Override default save method"""
        super().save(*args, **kwargs)


class RoomPhoto(models.Model):
    title = models.CharField(max_length=255, blank=True)
    image = models.ImageField(upload_to='room_photos')
    room = models.ForeignKey(
        Room, on_delete=models.CASCADE, null=True, blank=True,)

    class Meta:
        verbose_name_plural = 'Room Photos'

    def __str__(self):
        """Prints the name of the Photo"""
        return f'{self.room} photos'




class HostelBooking(HostelsModel):
    hostel = models.ForeignKey(Hostel , on_delete=models.CASCADE)
    no_gust = models.IntegerField()
    hostel_name = models.CharField(max_length=100)
    user = models.ForeignKey(UserAccount, related_name="users_booking" , on_delete=models.CASCADE)
    client_name = models.CharField(max_length=100)
    hostel = models.ForeignKey(Hostel, on_delete=models.CASCADE)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    chek_in=models.BooleanField()
    chek_out=models.BooleanField()
    c_type = models.CharField(max_length=100)
    prics = models.IntegerField(null=True, blank=True)
    # booking_type= models.CharField(max_length=100,choices=(('Pre Paid' , 'Pre Paid') , ('Post Paid' , 'Post Paid')))


class Rating(models.Model):
        hostel = models.ForeignKey(Hostel, related_name='rating',
                                    on_delete=models.CASCADE)
        name = models.CharField(max_length=100)
        image = models.CharField(max_length=900)
        one = models.PositiveIntegerField(default=0, null=True, blank=True)
        two = models.PositiveIntegerField(default=0, null=True, blank=True)
        three = models.PositiveIntegerField(default=0, null=True, blank=True)
        four = models.PositiveIntegerField(default=0, null=True, blank=True)
        five = models.PositiveIntegerField(default=0, null=True, blank=True)
        review = models.CharField(max_length=255, null=True, blank=True)

        class Meta:
          ordering = ['hostel']
