from django.db import models
from accounts.models import UserAccount


class FavouritHotel(models.Model):
        hotel = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
        id_no= models.IntegerField()
        class Meta:
          ordering = ['hotel']


class FavouritHostel(models.Model):
        hostel = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
        id_no= models.IntegerField()
        class Meta:
          ordering = ['hostel']



class FavouritHouse(models.Model):
        house = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
        id_no= models.IntegerField()
        class Meta:
          ordering = ['house']



class FavouritTripComp(models.Model):
        tripComp = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
        id_no= models.IntegerField()
        class Meta:
          ordering = ['tripComp']



class FavouritGuider(models.Model):
        guider = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
        id_no= models.IntegerField()
        class Meta:
          ordering = ['guider']