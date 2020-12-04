from django.urls import path, include
from .views import HomeView, WeatherApi

urlpatterns = [

    path('', HomeView.as_view(), name='home'),
    path('api/weather/', WeatherApi.as_view(), name='aaa'),
]