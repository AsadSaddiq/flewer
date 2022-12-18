from django.urls import path
from .views import *
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('api/create/', housecreate.as_view()),
    path('review/create/', Ratcreate.as_view()),
    path('api/retrieve/<int:pk>/', houseRetrieve.as_view()),
    path('fav/api/retrieve/<int:pk>/', favhouseRetrieve.as_view()),
    path('rating/retrieve/<int:pk>/', RatingHouse.as_view()),
    path('review/retrieve/<int:pk>/', RatRetrieve.as_view()),
    path('api/retrieve/', houseRetrieve.as_view()),
    path('review/retrieve/', RatRetrieve.as_view()),
    path('api/update/<int:pk>/', houseUpdate.as_view()),
    path('rating/update/<int:pk>/', RatingUpdate.as_view()),
    path('api/delete/<int:pk>/', houseDestroy.as_view()),
    path('images/api/', houseImgapi.as_view()),
    path('images/upload/', houseImgaUpload.as_view()),
    path('images/api/<int:pk>/', houseImgapi.as_view()),
    path('images/delete/<int:pk>/', houseImgapiDelete.as_view()),
    path('room/create/', RoomCreate.as_view()),
    path('room/retrieve/', RoomRetrieve.as_view()),
    path('room/retrieve/<int:pk>/', RoomRetrieve.as_view()),
    path('room/delete/<int:pk>/', RoomDestroy.as_view()),
    path('room/update/<int:pk>/', RoomUpdate.as_view()),
    path('room/images/api/', roomImgapi.as_view()),
    path('room/images/upload/', roomImgaUpload.as_view()),
    path('room/images/api/<int:pk>/', roomImgapi.as_view()),
    path('room/images/delete/<int:pk>/', roomImgapiDelete.as_view()),
    path('api/house/booking/', houseBooking.as_view()),
    path('api/house/booked/<int:pk>/', bookdate.as_view()),
    path('api/all/room/booked/<int:pk>/', allroombookdate.as_view()),
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)


urlpatterns += staticfiles_urlpatterns()