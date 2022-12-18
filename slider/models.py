from django.db import models


class SliderImages(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    image = models.ImageField(upload_to='hotels')
    description = models.CharField(max_length=512, blank=True, null=True)