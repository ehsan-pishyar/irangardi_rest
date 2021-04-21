from .models import State, City, HistoricalPlace
from .serializers import StateSerializer, CitySerializer, HistoricalPlaceSerializer
from rest_framework import viewsets


class GetStateList(viewsets.ModelViewSet):
    serializer_class = StateSerializer
    queryset = State.objects.all()


class GetCityList(viewsets.ModelViewSet):
    serializer_class = CitySerializer
    queryset = City.objects.all()


class GetHistoricalPlaceList(viewsets.ModelViewSet):
    serializer_class = HistoricalPlaceSerializer
    queryset = HistoricalPlace.objects.all()
