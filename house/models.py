from distutils.command.upload import upload
# from django.contrib.auth.models import User
from django.db import models
from accounts.models import UserAccount


class HouseModel(models.Model):
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now_add=True)

    class Meta:
        abstract = True



class House(HouseModel):
    # id = models.UUIDField(default=uuid.uuid4   , editable=False , primary_key=True)
    house= models.ForeignKey(UserAccount ,related_name="HouseModel", on_delete=models.CASCADE)
    house_name= models.CharField(max_length=100)
    description = models.TextField()
    location= models.CharField(max_length=100)
    longitude= models.CharField(max_length=100)
    latitude= models.CharField(max_length=100)
    guests=models.IntegerField()
    bed_count=models.IntegerField()
    room_count = models.IntegerField(default=10)
    bathroom_count=models.IntegerField()
    security_cameras=models.BooleanField()
    weapons=models.BooleanField()
    dangerous_animals=models.BooleanField()
    c_type=models.CharField(max_length=20, blank=True, null=True)
    house_price = models.IntegerField()
    is_apartment = models.BooleanField(default=False)
    free_wifi = models.BooleanField(default=False)
    refrigerator = models.BooleanField(default=False)
    telephone = models.BooleanField(default=False)
    ironing_facilities = models.BooleanField(default=False)
    wake_up_service = models.BooleanField(default=False)
    electric_kettle = models.BooleanField(default=False)
    tea_coffee_maker = models.BooleanField(default=False)
    daily_housekeeping = models.BooleanField(default=False)
    city_view = models.BooleanField(default=False)
    one = models.PositiveIntegerField(default=0, null=True, blank=True)
    two = models.PositiveIntegerField(default=0, null=True, blank=True)
    three = models.PositiveIntegerField(default=0, null=True, blank=True)
    four = models.PositiveIntegerField(default=0, null=True, blank=True)
    five = models.PositiveIntegerField(default=0, null=True, blank=True)


    def __str__(self) -> str:
        return self.house_name




class HouseImages(HouseModel):
    house= models.ForeignKey(House ,related_name="House_images", on_delete=models.CASCADE)
    images = models.ImageField(upload_to="house")





class Room(models.Model):
    """Creates room details"""

    house = models.ForeignKey(House, on_delete=models.CASCADE )
    room_photo = models.ImageField(default='default.jpg', upload_to='room_photos')
    room_Name = models.CharField(max_length=200)
    room_details = models.CharField(max_length=500)
    max_adults = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    # Room ammenities
    free_toiletries = models.BooleanField(default=False)
    safe_deposit_box = models.BooleanField(default=False)
    lcd_tv = models.BooleanField(default=False)
    pay_tv = models.BooleanField(default=False)
    mini_bar = models.BooleanField(default=False)
    blackout_drapes = models.BooleanField(default=False)
    desk = models.BooleanField(default=False)
    hair_dryer = models.BooleanField(default=False)
    extra_towels = models.BooleanField(default=False)
    bathrobes = models.BooleanField(default=False)
    warddrobe = models.BooleanField(default=False)
    toilet_paper = models.BooleanField(default=False)
    slippers = models.BooleanField(default=False)
    toilet = models.BooleanField(default=False)
    alarm_clock = models.BooleanField(default=False)
    bathtub_shower = models.BooleanField(default=False)
    makeup_shaving_mirror = models.BooleanField(default=False)
    air_conditioner = models.BooleanField(default=False)
    garden_view = models.BooleanField(default=False)

    
    class Meta:
      
        ordering = ['room_Name', 'updated_at', ]

    def __str__(self):
        return f'({self.room_Name})-{self.house.house_name}'

    
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


class HouseBooking(models.Model):
    # house = models.ForeignKey(House  , related_name="House_bookings" , on_delete=models.CASCADE)
    house_name = models.CharField(max_length=100)
    user = models.ForeignKey(UserAccount , on_delete=models.CASCADE)
    client_name = models.CharField(max_length=100)
    house = models.ForeignKey(House, on_delete=models.CASCADE)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    chek_in=models.BooleanField()
    chek_out=models.BooleanField()
    c_type = models.CharField(max_length=100)
    prics = models.IntegerField(null=True, blank=True)



class Rating(models.Model):
        house = models.ForeignKey(House, related_name='rating',
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
          ordering = ['house']

        