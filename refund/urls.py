from django.urls import path
from .views import *


urlpatterns = [   
    # path('api/retrieve/<int:pk>/', CityRetrieve.as_view()),
    path('api/retrieve/', RefundRetrieve.as_view()),
    
]

