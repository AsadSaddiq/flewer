from django.urls import path
from .views import *
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('comp/create/', compcreate.as_view()),
    path('comp/review/create/', CompRatcreate.as_view()),
    path('guider/review/create/', GuiRatcreate.as_view()),
    path('comp/retrieve/<int:pk>/', compRetrieve.as_view()),
    path('comp/review/retrieve/<int:pk>/', CompRatRetrieve.as_view()),
    path('guider/review/retrieve/<int:pk>/', GuiRatRetrieve.as_view()),
    path('comp/rating/retrieve/<int:pk>/', RatingCompany.as_view()),
    path('comp/retrieve/', compRetrieve.as_view()),
    path('comp/review/retrieve/', CompRatRetrieve.as_view()),
    path('guider/review/retrieve/', GuiRatRetrieve.as_view()),
    path('comp/update/<int:pk>/', compUpdate.as_view()),
    path('comp/rating/update/<int:pk>/', RatingUpdate.as_view()),
    path('comp/delete/<int:pk>/', compDestroy.as_view()),
    path('api/create/', tripcreate.as_view()),
    path('api/retrieve/<int:pk>/', tripRetrieve.as_view()),
    path('api/retrieve/', tripRetrieve.as_view()),
    path('api/update/<int:pk>/', tripUpdate.as_view()),
    path('api/delete/<int:pk>/', tripDestroy.as_view()),
    path('img/create/', tripImagescreate.as_view()),
    path('img/retrieve/<int:pk>/', tripImagesRetrieve.as_view()),
    path('img/retrieve/', tripImagesRetrieve.as_view()),
    path('img/update/<int:pk>/', tripImagesUpdate.as_view()),
    path('img/delete/<int:pk>/', tripImagesDestroy.as_view()),
    path('guider/create/', tripguidercreate.as_view()),
    path('guider/retrieve/<int:pk>/', tripguiderRetrieve.as_view()),
    path('guider/rating/retrieve/<int:pk>/', RatingGuider.as_view()),
    path('guider/retrieve/', tripguiderRetrieve.as_view()),
    path('guider/update/<int:pk>/', tripguiderUpdate.as_view()),
    path('guider/rating/update/<int:pk>/', GuiderRatingUpdate.as_view()),
    path('guider/delete/<int:pk>/', tripguiderDestroy.as_view()),
    path('api/guider/booking/', tripGuiderBooking.as_view()),
    path('api/comp/booking/', comptripbooking.as_view()),
    path('api/guider/booked/<int:pk>/', bookdate.as_view()),
    path('api/trip/booked/<int:pk>/', tripbookdate.as_view()),
    path('fav/comp/retrieve/<int:pk>/', favCompRetrieve.as_view()),
    path('fav/guider/retrieve/<int:pk>/', favGuiderRetrieve.as_view()),
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)


urlpatterns += staticfiles_urlpatterns()