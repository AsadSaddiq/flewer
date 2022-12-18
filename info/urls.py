from django.urls import path
from .views import *


urlpatterns = [   
    # path('api/retrieve/<int:pk>/', CityRetrieve.as_view()),
    path('privecypolicy/retrieve/', PrivecyPolicyRetrieve.as_view()),
    path('termservice/retrieve/', TermServiceRetrieve.as_view()),
]

