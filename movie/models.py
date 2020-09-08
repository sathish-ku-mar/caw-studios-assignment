from django.db import models
from account.models import CommonModel
# Create your models here.


class Movie(CommonModel):
    """
    This model is used to store the movie details.
    """
    name = models.CharField(max_length=200, help_text='The name of the movie')
    language = models.CharField(max_length=200, help_text='The audio language of the movie')
    cast = models.CharField(max_length=200, null=True, blank=True, help_text='The group of actors who make up a movie')
    director = models.CharField(max_length=200,null=True, blank=True,
                                help_text='A person name who controls the making of a movie')
    duration = models.FloatField(max_length=200, null=True, blank=True,
                                 help_text='Running time of a movie by hours')

    class Meta:
        ordering = ['-id', ]
        verbose_name_plural = 'Movies'
        db_table = 'movie'
        get_latest_by = "-created_at"
        verbose_name = "Movie"

    def __str__(self):
        return str(self.name)

    @classmethod
    def get_movies_all(cls):
        """
        Get all the movies
        :param: None
        :return: Movie object
        :rtype: django.db.models.query.QuerySet
        """
        return cls.objects.filter(is_active=True)

    @classmethod
    def get_movies_by_ids(cls, ids):
        """
        Get all the movies
        :param ids: Get the list of movie ids
        :return: Movie object
        :rtype: django.db.models.query.QuerySet
        """
        return cls.objects.filter(id__in=ids)

    def set_is_not_active(self):
        """
        Set active as false to remove the movie
        """
        self.is_active = False
        self.save(update_fields=['is_active'])