from django.shortcuts import get_object_or_404
from .models import Show
from .serializers import ShowSerializer
from movie.serializers import MovieSerializer
from rest_framework import status, viewsets
from rest_framework.response import Response
from django.http.request import QueryDict


class ShowViewSet(viewsets.ViewSet):
    """
        A simple ViewSet for the shows.
    """
    model = Show
    serializer_class = ShowSerializer
    queryset = model.get_shows_all()

    def get_all_movies_by_city(self, request, city_name):
        """
            To get all movies by city
            URL Structure: /cinema/by-city/Bengaluru/
            Required Fields: id
        """
        queryset = self.model.get_all_movies_by_city(city_name)
        serializer = MovieSerializer(queryset, many=True)
        return Response(serializer.data)

    def get_all_cinemas_along_with_showtimes_by_movie(self, request, movie_id):
        """
            To get all cinemas along with showtimes by movie
            URL Structure: /cinema/by-movie/1/
            Required Fields: id
        """
        queryset = self.model.get_all_cinemas_along_with_showtimes_by_movie(movie_id)
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)

    def get_availabe_seats_by_showtimes(self, request, show_id):
        """
            To get available seats by showtimes
            URL Structure: /cinema/by-showtimes/1/
            Required Fields: id
        """
        queryset = self.model.get_availabe_seats_by_showtimes(show_id)
        return Response({'available': queryset})

