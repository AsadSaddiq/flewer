from django.urls import path
from .views import *
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('history/create/', historycreate.as_view()),
    path('history/<int:pk>/', S_History.as_view()),
    path('owner/history/<int:pk>/', O_History.as_view()),
    path('booker/history/<int:pk>/', B_History.as_view()),
   
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
