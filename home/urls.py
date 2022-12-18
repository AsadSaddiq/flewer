# from django import views
from django.urls import path

from .views import *
from . import views
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('api/create/', hotelcreate.as_view()),
    path('review/create/', Ratcreate.as_view()),
    path('api/retrieve/<int:pk>/', hotelRetrieve.as_view()),
    path('fav/api/retrieve/<int:pk>/', favhotelRetrieve.as_view()),
    path('review/retrieve/<int:pk>/', RatRetrieve.as_view()),
    path('rating/retrieve/<int:pk>/', RatingHotel.as_view()),
    path('api/retrieve/', hotelRetrieve.as_view()),
    path('review/retrieve/', RatRetrieve.as_view()),
    path('api/update/<int:pk>/', hotelUpdate.as_view()),
    path('rating/update/<int:pk>/', RatingUpdate.as_view()),
    path('api/delete/<int:pk>/', hotelDestroy.as_view()),
    path('images/api/', hotelImgapi.as_view()),
    path('images/upload/', hotelImgaUpload.as_view()),
    path('images/api/<int:pk>/', hotelImgapi.as_view()),
    path('images/delete/<int:pk>/', hotelImgapiDelete.as_view()),
    path('room/create/', RoomCreate.as_view()),
    path('room/retrieve/', RoomRetrieve.as_view()),
    path('room/retrieve/<int:pk>/', RoomRetrieve.as_view()),
    path('room/delete/<int:pk>/', RoomDestroy.as_view()),
    path('room/update/<int:pk>/', RoomUpdate.as_view()),
    path('room/images/api/', roomImgapi.as_view()),
    path('room/images/upload/', roomImgaUpload.as_view()),
    path('room/images/api/<int:pk>/', roomImgapi.as_view()),
    path('room/images/delete/<int:pk>/', roomImgapiDelete.as_view()),
    path('api/room/booking/', hotelRoomBooking.as_view()),
    path('api/room/booked/<int:pk>/', bookdate.as_view()),
    path('api/all/room/booked/<int:pk>/', allroombookdate.as_view()),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
