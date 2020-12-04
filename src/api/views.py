from django.views.generic import View
from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from . import serializers
import requests
import json
# Create your views here.


class HomeView(View):

    def get(self, request, *args, **Kwargs):
        return render(request, 'api/api_weather.html')

    def post(self, request, *args, **Kwargs):
        context = {}
        city = request.POST.get('city')
        numberOfDays = request.POST.get('numberOfDays')
        base_url = 'http://lukhanyo.pythonanywhere.com/'
        endpoint_path = f'api/read/'
        url = f'{base_url}{endpoint_path}'
        result = requests.post(url, data={'city': city, 'numberOfDays': numberOfDays})

        y = json.loads(result.text)
        context['city'] = city
        context['label'] = y['city']
        context['forecast'] = y['output'][0]
        context['numberOfDays'] = numberOfDays

        return render(request, 'api/api_weather.html',  context=context)

class WeatherApi(APIView):
    authentication_classes = []
    permission_classes = []
    serializer_class = serializers.WeatherApiSerializer

    def get(self, request, format=None):
        data = {}
        return Response(data)

