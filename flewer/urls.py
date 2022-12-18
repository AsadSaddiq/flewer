
from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.conf.urls.static import static
from django.conf import settings


schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path('social/auth/', include('djoser.social.urls')),
    # path('api/user/', include('accounts.urls')),
    path('hotel/', include('home.urls')),
    path('info/', include('info.urls')),
    path('report/', include('reportapp.urls')),
    path('refund/', include('refund.urls')),
    path('city/', include('city.urls')),
    path('house/', include('house.urls')),
    path('hostel/', include('hostels.urls')),
    path('trip/', include('tripapp.urls')),
    path('chatapi/', include('chat.urls')),
    path('slider/', include('slider.urls')),
    path('payment/', include('payment.urls')),
    path('favourit/', include('favourit.urls')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

