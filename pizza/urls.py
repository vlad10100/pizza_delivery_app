
from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi




schema_view = get_schema_view(
   openapi.Info(
      title="Pizza Delivery API",
      default_version='v8',
      description="Pizza Delivery API",
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('swagger<format>.json|.yaml/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    path('admin/', admin.site.urls),
    path('auth/', include('authentication.urls', namespace='authentication')),
    path('orders/', include('orders.urls', namespace='orders')),
    path('auth/', include('djoser.urls.jwt')),
]
