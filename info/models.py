from django.db import models
from tinymce.models import HTMLField


class PrivecyPolicy(models.Model):
    title = models.CharField(max_length=999)
    # privaceypolicy = models.TextField(max_length=999)
    privaceypolicy = HTMLField(blank=True, null=True)
   

class TermService(models.Model):
    title = models.CharField(max_length=999)
    # privaceypolicy = models.TextField(max_length=999)
    TermServices = HTMLField(blank=True, null=True)