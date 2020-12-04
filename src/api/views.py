from django.views.generic import View
from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer
from . import serializers
from rest_framework import status as st
import requests
import json
# Create your views here.


def home_view(request):
    context = {}

    return render(request, 'api/api_weather.html',)


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

        data = {
            "eee": "eee",
            "labels": ['Red', 'Blue', 'Yellow', 'Green', 'Purple', 'Orange'],
            "default": [3,5,8,9,10],
        }
        return render(request, 'api/api_weather.html',  context=context)

class WeatherApi(APIView):
    # renderer_classes = [TemplateHTMLRenderer]
    authentication_classes = []
    permission_classes = []
    serializer_class = serializers.WeatherApiSerializer

    def get(self, request, format=None):
        pass
        data = {}
        return Response(data)


    # def post(self, request):
    #     """ Requested weather results"""
    #     serializer = self.serializer_class(data=request.data)
    #     if serializer.is_valid():
    #
    #         api = ['post', 'post2']
    #         city = serializer.validated_data.get('city')
    #         numberOfDays = serializer.validated_data.get('numberOfDays')
    #         msg = f'City {city} - {numberOfDays}'
    #
    #         default = [12, 19, 3, 5, 2, 3]
    #         labels = ['Red', 'Blue', 'Yellow', 'Green', 'Purple', 'Orange']
    #
    #         data = {
    #             "labels": labels,
    #             "default": default,
    #         }
    #
    #         return Response(data)
    #
    #     else:
    #         return Response(serializer.errors,
    #                         status=st.HTTP_400_BAD_REQUEST
    #                         )