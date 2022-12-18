from django.db import models
from accounts.models import UserAccount




class PaymentHistory(models.Model):
    superuser = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    owner_id = models.IntegerField()
    Place_name = models.CharField(max_length=100)
    Room_House_No = models.CharField(max_length=100)
    booker_id = models.IntegerField()
    booker_name = models.CharField(max_length=100)
    owner_name = models.CharField(max_length=100)
    c_type = models.CharField(max_length=100)
    amount= models.IntegerField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    booking_date = models.DateTimeField(auto_now_add=True)