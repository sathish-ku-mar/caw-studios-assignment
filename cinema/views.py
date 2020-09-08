from django.shortcuts import get_object_or_404
from .models import Show
from .serializers import ShowSerializer
from movie.serializers import MovieSerializer
from rest_framework import status, viewsets
from rest_framework.response import Response
from django.http.request import QueryDict


class ShowViewSet(viewsets.ViewSet):
    """
        A simple ViewSet for the movies.
    """
    model = Show
    serializer_class = ShowSerializer
    queryset = model.get_shows_all()

    def get_all_movies_by_city(self, request, city_name):
        """
            To update the particular movie
            URL Structure: /movie/1/
            Required Fields: id
        """
        queryset = self.model.get_all_movies_by_city(city_name)
        print(queryset)
        serializer = MovieSerializer(queryset, many=True)
        return Response(serializer.data)

    def get_all_cinemas_along_with_showtimes_by_movie(self, request, movie_id):
        """
            To update the particular movie
            URL Structure: /movie/1/
            Required Fields: id
        """
        queryset = self.model.get_all_cinemas_along_with_showtimes_by_movie(movie_id)
        print(queryset)
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)

    # def list(self, request):
    #     """
    #         To list the movies
    #         URL Structure: /movie/
    #         Required Fields: None
    #     """
    #
    #     queryset = self.model.get_movies_all()
    #     serializer = self.serializer_class(queryset, many=True)
    #     return Response(serializer.data)
    #
    # def retrieve(self, request, pk):
    #     """
    #         To update the particular movie
    #         URL Structure: /movie/1/
    #         Required Fields: id
    #     """
    #     queryset = get_object_or_404(self.model, id=pk)
    #     serializer = self.serializer_class(queryset, many=False)
    #     return Response(serializer.data)
    #
    # def create(self, request):
    #     """
    #         To create the movies
    #         URL Structure: /movie/
    #         Required Fields: name, language, cast, director, duration
    #     """
    #     # For create movie
    #     data = QueryDict.dict(request.data)
    #     serializer = self.serializer_class(data=data)
    #
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    #
    # def update(self, request, pk):
    #     """
    #         To update the particular movie
    #         URL Structure: /movie/1/
    #         Required Fields: 'id', 'name', 'director', 'genre', 'popularity','imdb_score'
    #     """
    #     queryset = get_object_or_404(self.model, id=pk)
    #     data = QueryDict.dict(request.data)
    #     serializer = self.serializer_class(queryset, data=data, partial=True)
    #
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(serializer.errors, status=400)
    #
    # def delete(self, request, pk):
    #     """
    #         To delete the particular movie
    #         URL Structure: /movie/1/
    #         Required Fields: id
    #     """
    #     queryset = get_object_or_404(self.model, id=pk)
    #     queryset.set_is_not_active()
    #
    #     return Response({'message': 'Deleted'}, status=200)