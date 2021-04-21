from django.db import models


class HistoricalPlace(models.Model):
    hp_name = models.CharField(max_length=100, blank=True, null=True)
    hp_image = models.ImageField(blank=True, null=True)
    hp_latitude = models.IntegerField(blank=True, null=True)
    hp_longitude = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.hp_name


class City(models.Model):
    city_name = models.CharField(max_length=50, blank=False, null=False)
    city_population = models.IntegerField(null=False, blank=False)
    city_language = models.CharField(max_length=50, blank=False, null=False)
    historical_places = models.ManyToManyField(HistoricalPlace)

    def __str__(self):
        return self.city_name


class State(models.Model):
    state_name = models.CharField(max_length=50, blank=False, null=False)
    state_center = models.CharField(max_length=50, blank=False, null=False)
    state_population = models.IntegerField(null=False, blank=False)
    state_cities = models.ManyToManyField(City)

    def __str__(self):
        return self.state_name


