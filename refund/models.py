from django.db import models
from tinymce.models import HTMLField


class Refund(models.Model):
    title = models.CharField(max_length=999)
    refund = HTMLField(blank=True, null=True)