# Generated by Django 3.1.2 on 2020-11-11 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_basics', '0002_auto_20201109_1956'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='historicalplacesfields',
            name='historical_place',
        ),
        migrations.RemoveField(
            model_name='localfoodfields',
            name='local_food',
        ),
        migrations.RemoveField(
            model_name='religiousplacefields',
            name='religious_place',
        ),
        migrations.RemoveField(
            model_name='souvenirfields',
            name='souvenir',
        ),
        migrations.RemoveField(
            model_name='tourismplacefields',
            name='tourism_place',
        ),
        migrations.AddField(
            model_name='city',
            name='historical_places',
            field=models.ManyToManyField(to='api_basics.HistoricalPlace'),
        ),
        migrations.AddField(
            model_name='state',
            name='state_cities',
            field=models.ManyToManyField(to='api_basics.City'),
        ),
        migrations.DeleteModel(
            name='CityFields',
        ),
        migrations.DeleteModel(
            name='HistoricalPlacesFields',
        ),
        migrations.DeleteModel(
            name='LocalFood',
        ),
        migrations.DeleteModel(
            name='LocalFoodFields',
        ),
        migrations.DeleteModel(
            name='ReligiousPlace',
        ),
        migrations.DeleteModel(
            name='ReligiousPlaceFields',
        ),
        migrations.DeleteModel(
            name='Souvenir',
        ),
        migrations.DeleteModel(
            name='SouvenirFields',
        ),
        migrations.DeleteModel(
            name='TourismPlace',
        ),
        migrations.DeleteModel(
            name='TourismPlaceFields',
        ),
    ]
