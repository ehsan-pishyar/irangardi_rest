from rest_framework import serializers
from .models import State, City, HistoricalPlace


class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = State
        # fields = ['name', 'state_center', 'population']
        fields = '__all__'


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'


class HistoricalPlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistoricalPlace
        fields = '__all__'

"""
class ReligiousPlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReligiousPlace
        fields = '__all__'


class TourismPlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = TourismPlace
        fields = '__all__'


class LocalFoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = LocalFood
        fields = '__all__'


class SouvenirSerializer(serializers.ModelSerializer):
    class Meta:
        model = Souvenir
        fields = '__all__'
"""