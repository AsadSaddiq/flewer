from django.urls import path
from .views import *


urlpatterns = [   
    # path('api/retrieve/<int:pk>/', CityRetrieve.as_view()),
    path('api/create/', ReportCreate.as_view()),
]

