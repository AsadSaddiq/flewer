# from django import views
from django.urls import path
from .views import *
from .views import hostelRoomBooking
from django.conf import settings


urlpatterns = [
    path('api/create/', hostelcreate.as_view()),
    path('review/create/', Ratcreate.as_view()),
    path('api/retrieve/<int:pk>/', hostelRetrieve.as_view()),
    path('fav/api/retrieve/<int:pk>/', favhostelRetrieve.as_view()),
    path('review/retrieve/<int:pk>/', RatRetrieve.as_view()),
    path('rating/retrieve/<int:pk>/', RatingHostel.as_view()),
    path('api/retrieve/', hostelRetrieve.as_view()),
    path('review/retrieve/', RatRetrieve.as_view()),
    path('api/update/<int:pk>/', hostelUpdate.as_view()),
    path('rating/update/<int:pk>/', RatingUpdate.as_view()),
    path('api/delete/<int:pk>/', hostelDestroy.as_view()),
    path('images/api/', hostelImgapi.as_view()),
    path('images/upload/', hostelImgaUpload.as_view()),
    path('images/api/<int:pk>/', hostelImgapi.as_view()),
    path('images/delete/<int:pk>/', hostelImgapiDelete.as_view()),
    path('room/create/', RoomCreate.as_view()),
    path('room/retrieve/', RoomRetrieve.as_view()),
    path('room/retrieve/<int:pk>/', RoomRetrieve.as_view()),
    path('room/delete/<int:pk>/', RoomDestroy.as_view()),
    path('room/update/<int:pk>/', RoomUpdate.as_view()),
    path('room/images/api/', roomImgapi.as_view()),
    path('room/images/upload/', roomImgaUpload.as_view()),
    path('room/images/api/<int:pk>/', roomImgapi.as_view()),
    path('room/images/delete/<int:pk>/', roomImgapiDelete.as_view()),
    path('api/room/booking/', hostelRoomBooking.as_view()),
    # path('api/room/booked/<int:pk>/', bookdate.as_view()),
    path('api/all/room/booked/<int:pk>/', allroombookdate.as_view()),

]
