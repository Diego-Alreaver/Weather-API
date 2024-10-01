from django.urls import path
from .views import HomeView, WeatherView 
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.urls import path, include

schema_view = get_schema_view(
    openapi.Info(
        title="Alreavers Weather API",
        default_version='v1',
        description="API para obtener datos del clima",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@weather.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('', HomeView.as_view(), name='home'),
    path('weather/', WeatherView.as_view(), name='get_weather'),
]
