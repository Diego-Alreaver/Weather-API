import os
import json
import requests
import redis
from dotenv import load_dotenv
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from django.http import JsonResponse



# Cargar variables de entorno
load_dotenv()

# Obtener la API key desde el archivo .env
WEATHER_API_KEY = os.getenv('WEATHER_API_KEY')

class HomeView(APIView):
    def get(self, request):
        return Response({'message': 'Welcome to the Alreavers Weather API!'})

class WeatherView(APIView):
    """
    Obtener los datos del clima para una ciudad específica.
    **Parámetros**:
    - city: Nombre de la ciudad a consultar (opcional, por defecto: London).
    **Respuesta**:
    - 200: Datos del clima en formato JSON.
    - 500: Error si no se pueden obtener los datos.
    """
    
    @swagger_auto_schema(
        operation_description="Obtener los datos del clima para una ciudad específica.",
        manual_parameters=[
            openapi.Parameter('city', openapi.IN_QUERY, description="Nombre de la ciudad a consultar (opcional, por defecto: London).", type=openapi.TYPE_STRING)
        ]
    )

    def get(self, request):
        city = request.GET.get('city', 'London')
        cached_weather = redis_client.get(city)

        if cached_weather:
            return Response({'source': 'cache', 'data': json.loads(cached_weather)})

        url = f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{city}?unitGroup=metric&key={WEATHER_API_KEY}"
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            weather_data = {
                "city": data['address'],
                "temperature": f"{data['currentConditions']['temp']}°C",
                "description": data['currentConditions']['conditions'],
                "humidity": f"{data['currentConditions']['humidity']}%"
            }
            redis_client.setex(city, 43200, json.dumps(weather_data))
            return Response(weather_data)
        else:
            return Response({'error': 'Could not fetch weather data'}, status=500)

# Conexión a Redis para el caching
redis_client = redis.StrictRedis(
    host=os.getenv('REDIS_HOST', 'localhost'),
    port=os.getenv('REDIS_PORT', 6379),
    db=0,
    decode_responses=True
)
