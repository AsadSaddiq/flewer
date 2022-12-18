from django.db import models

class City(models.Model):
    city= models.CharField(max_length=100)
    location= models.CharField(max_length=300)
   
    

    def __str__(self) -> str:
        return self.city
