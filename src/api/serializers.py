from rest_framework import serializers


class WeatherApiSerializer(serializers.Serializer):
    """Weather request serializer"""

    city = serializers.CharField()
    numberOfDays = serializers.IntegerField(min_value=1, max_value=7)

