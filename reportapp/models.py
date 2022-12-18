from django.db import models
from accounts.models import UserAccount


class Report(models.Model):
    Place_name = models.CharField(max_length=100)
    place_id = models.CharField(max_length=100)
    reporter_id = models.CharField(max_length=100)
    reporter_name = models.CharField(max_length=100)
    report = models.TextField()
    
    
    