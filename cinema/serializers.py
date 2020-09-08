from rest_framework import serializers
from .models import Cinema, Show
from movie.serializers import MovieSerializer

class CinemaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cinema
        fields = ('id', 'name', 'city', 'address')
        read_only_fields = ('id',)


class ShowSerializer(serializers.ModelSerializer):
    cinema = CinemaSerializer()
    movie = MovieSerializer()

    class Meta:
        model = Show
        fields = ('id', 'cinema', 'movie', 'screen', 'date', 'time')