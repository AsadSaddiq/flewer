from django.urls import path
from .views import *


urlpatterns = [
    
    path('api/retrieve/<int:pk>/', ImagesRetrieve.as_view()),
    path('api/retrieve/', ImagesRetrieve.as_view()),
   
]

