# from django import views
from django.urls import path

from .views import *
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    # HOTEL
    path('hotel/create/', favhotelcreate.as_view()),
    path('hotel/retrieve/<int:pk>/', favhotelRetrieve.as_view()),
    path('hotel/delete/<int:hotel>/<int:owner>/', favhotelDestroy.as_view()),
    # HOSTEL
    path('hostel/create/', favhostelcreate.as_view()),
    path('hostel/retrieve/<int:pk>/', favhostelRetrieve.as_view()),
    path('hostel/delete/<int:hostel>/<int:owner>/', favhostelDestroy.as_view()),
    # Guider
    path('guider/create/', favGuidercreate.as_view()),
    path('guider/retrieve/<int:pk>/', favGuiderRetrieve.as_view()),
    path('guider/delete/<int:guider>/<int:owner>/', favGuiderDestroy.as_view()),
    # HOUSE
    path('comp/create/', favTripCompcreate.as_view()),
    path('comp/retrieve/<int:pk>/', favTripCompRetrieve.as_view()),
    path('comp/delete/<int:comp>/<int:owner>/', favTripCompDestroy.as_view()),
    # HOUSE
    path('house/create/', favhousecreate.as_view()),
    path('house/retrieve/<int:pk>/', favhouseRetrieve.as_view()),
    path('house/delete/<int:guider>/<int:owner>/', favhouseDestroy.as_view()),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
