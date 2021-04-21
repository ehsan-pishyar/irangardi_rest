from django.urls import path, include
from .views import GetStateList, GetCityList, GetHistoricalPlaceList
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'states', GetStateList)
router.register(r'cities', GetCityList)
router.register(r'historical-places', GetHistoricalPlaceList)

urlpatterns = [
    path('', include(router.urls)),
]