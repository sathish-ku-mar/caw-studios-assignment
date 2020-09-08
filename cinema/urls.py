from django.urls import path,include
from django.conf.urls import url

from .views import ShowViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', ShowViewSet)


urlpatterns = [
    path(r'by-city/<str:city_name>/', ShowViewSet.as_view({'get': 'get_all_movies_by_city'}), name='get_all_movies_by_city'),
    path(r'by-movie/<int:movie_id>/', ShowViewSet.as_view({'get': 'get_all_cinemas_along_with_showtimes_by_movie'}),
         name='get_all_cinemas_along_with_showtimes_by_movie'),
    path(r'by-showtimes/<int:show_id>/', ShowViewSet.as_view({'get': 'get_availabe_seats_by_showtimes'}),
         name='get_availabe_seats_by_showtimes'),

]

urlpatterns += router.urls