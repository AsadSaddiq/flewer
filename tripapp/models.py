from django.db import models
from accounts.models import UserAccount

class TripComp(models.Model):
    owner_id= models.ForeignKey(UserAccount , on_delete=models.CASCADE)
    com_name=models.CharField(max_length=50)
    com_img=models.ImageField(upload_to="comp")
    owner_name=models.CharField(max_length=50)
    about_comp=models.TextField()
    one = models.PositiveIntegerField(default=0, null=True, blank=True)
    two = models.PositiveIntegerField(default=0, null=True, blank=True)
    three = models.PositiveIntegerField(default=0, null=True, blank=True)
    four = models.PositiveIntegerField(default=0, null=True, blank=True)
    five = models.PositiveIntegerField(default=0, null=True, blank=True)

    def __str__(self) -> str:
        return self.com_name



class Trip(models.Model):
    trip_guider= models.ForeignKey(TripComp , on_delete=models.CASCADE)
    trip_name=models.CharField(max_length=50)
    start_date=models.DateField()
    end_date=models.DateField()
    duration=models.CharField(max_length=100)
    location=models.CharField(max_length=200)
    latitude=models.CharField(max_length=200)
    longitude=models.CharField(max_length=200)
    vistingPlaces=models.TextField()
    c_type=models.CharField(max_length=30)
    single_price=models.IntegerField()
    cuple_price=models.IntegerField()

    def __str__(self) -> str:
        return self.trip_name


class TripImages(models.Model):
    title = models.CharField(max_length=255, blank=True)
    image = models.ImageField(upload_to='trip_photos')
    place = models.ForeignKey(
        Trip, on_delete=models.CASCADE, null=True, blank=True,)

    def __str__(self) -> str:
        return self.title


class TripGuider(models.Model):
    trip_comp= models.ForeignKey(UserAccount , on_delete=models.CASCADE)
    name=models.CharField(max_length=50)
    image=models.ImageField(upload_to="tripGuid")
    about=models.TextField()
    location=models.CharField(max_length=99)
    latitude=models.CharField(max_length=200)
    longitude=models.CharField(max_length=200)
    c_type=models.CharField(max_length=200 , null=True, blank=True)
    price=models.IntegerField()
    one = models.PositiveIntegerField(default=0, null=True, blank=True)
    two = models.PositiveIntegerField(default=0, null=True, blank=True)
    three = models.PositiveIntegerField(default=0, null=True, blank=True)
    four = models.PositiveIntegerField(default=0, null=True, blank=True)
    five = models.PositiveIntegerField(default=0, null=True, blank=True)

    def __str__(self) -> str:
        return self.name



class CompRating(models.Model):
        comp = models.ForeignKey(TripComp, related_name='rating',
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
          ordering = ['comp']



class GuiRating(models.Model):
        guid = models.ForeignKey(TripGuider, related_name='rating',
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
          ordering = ['guid']


class TripBooking(models.Model):
    trip_comp = models.ForeignKey(TripComp, on_delete=models.CASCADE)
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE)
    trip_name = models.CharField(max_length=100)
    c_type = models.CharField(max_length=100)
    single_prics = models.IntegerField(null=True, blank=True)
    cuple_price = models.IntegerField(null=True, blank=True)
    user = models.ForeignKey(UserAccount , on_delete=models.CASCADE)
    client_name = models.CharField(max_length=100) 
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    chek_in=models.BooleanField()
    chek_out=models.BooleanField()


class GuiderBooking(models.Model):
    guider = models.ForeignKey(TripGuider, on_delete=models.CASCADE)
    guider_name = models.CharField(max_length=100)
    user = models.ForeignKey(UserAccount , on_delete=models.CASCADE)
    client_name = models.CharField(max_length=100) 
    c_type = models.CharField(max_length=100)
    single_prics = models.IntegerField(null=True, blank=True)
    cuple_price = models.IntegerField(null=True, blank=True)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    chek_in=models.BooleanField()
    chek_out=models.BooleanField()