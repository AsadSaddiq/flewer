# from django.contrib.auth.views import logout
# from django.urls import path
from . import views
from .views import *
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
   
    path('api/messages/<int:sender>/<int:receiver>/', message.as_view()),
    path('api/messages/', message_list.as_view()),
    path('api/useers/<int:pk>', user_list.as_view()),
    path('api/contact/list/<int:sender>/', contact_retrieve.as_view()),
    path('api/contact/', ContactList.as_view()), 
    
]
 

