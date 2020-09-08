from django.db import models
from account.models import CommonModel
# Create your models here.

from movie.models import Movie


class Cinema(CommonModel):
    """
    This model is used to store the cinema details.
    """
    name = models.CharField(max_length=200, help_text='The name of the cinema')
    city = models.CharField(max_length=200, help_text='The city of the cinema')
    address = models.CharField(max_length=200, help_text='The location of the cinema')

    class Meta:
        ordering = ['-id', ]
        verbose_name_plural = 'Cinemas'
        db_table = 'cinema'
        get_latest_by = "-created_at"
        verbose_name = "Cinema"

    def __str__(self):
        return str(self.name)

    @classmethod
    def get_cinemas_all(cls):
        """
        Get all the cinemas
        :param: None
        :return: Cinema object
        :rtype: django.db.models.query.QuerySet
        """
        return cls.objects.filter(is_active=True)

    @classmethod
    def get_all_cinema_by_city(cls, city_name):
        """
        Get all the cinemas by city
        :param city_name: get the name of the city
        :return: Cinema object
        :rtype: django.db.models.query.QuerySet
        """
        return cls.objects.filter(city=city_name)

    def set_is_not_active(self):
        """
        Set active as false to remove the cinema
        """
        self.is_active = False
        self.save(update_fields=['is_active'])


class Screen(CommonModel):
    """
    This model is used to store the cinema screen details.
    """
    name = models.CharField(max_length=200, help_text='The name of the screen')
    cinema = models.ForeignKey(Cinema, on_delete=models.CASCADE, null=True, blank=True,
                               help_text='The screen related with cinema')
    no_of_seats = models.DecimalField(max_digits=5, decimal_places=2,
                                      help_text='The number of the seats available in the screen')

    def __str__(self):
        return str(self.name)

    def get_no_of_seats(self):
        """
        Get the number seats in the screen
        :param: None
        :return: Number of seats
        :rtype: float
        """
        return self.no_of_seats


class SeatClass(models.Model):
    """
    This model is used to store the cinema seat class details.
    """
    name = models.CharField(max_length=200, help_text='The name of the seat class')
    cinema = models.ForeignKey(Cinema, on_delete=models.CASCADE, null=True, blank=True,
                               help_text='The name of the cinemas')

    def __str__(self):
        return str(self.name)


class Show(CommonModel):
    """
    This model is used to store the cinema show details.
    """
    cinema = models.ForeignKey(Cinema, on_delete=models.CASCADE, null=True, blank=True, help_text='The cinema related with show')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, null=True, blank=True, help_text='The movie related with show')
    screen = models.ForeignKey(Screen, on_delete=models.CASCADE, null=True, blank=True, related_name='shows_screen')
    date = models.DateField(help_text='The show date for the cinema')
    time = models.TimeField(help_text='The show time for the cinema')

    def __str__(self):
        return str(self.id)

    @classmethod
    def get_shows_all(cls):
        """
        Get all the shows
        :param: None
        :return: Show object
        :rtype: django.db.models.query.QuerySet
        """
        return cls.objects.filter(is_active=True)

    @classmethod
    def get_all_movies_by_city(cls, city_name):
        """
        Get all the movies by city
        :param city_name: get the name of the city
        :return: Show object
        :rtype: django.db.models.query.QuerySet
        """
        movie_ids = cls.objects.filter(cinema__city=city_name).values_list('movie', flat=True)
        return Movie.get_movies_by_ids(movie_ids)

    @classmethod
    def get_all_cinemas_along_with_showtimes_by_movie(cls, movie_id):
        """
        Get all the cinemas along with showtimes by movie
        :param movie_id: get the id of the movie
        :return: Show object
        :rtype: django.db.models.query.QuerySet
        """
        return cls.objects.filter(movie_id=movie_id)

    @classmethod
    def get_availabe_seats_by_showtimes(cls, show_id):
        """
        Get available seats by showtimes
        :param show_id: get the id of the show
        :return: Show object
        :rtype: django.db.models.query.QuerySet
        """
        from django.apps import apps

        return cls.objects.get(id=show_id).screen.get_no_of_seats() - apps.get_model('booking.Booking').get_booked_count(show_id)
