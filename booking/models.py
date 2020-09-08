from django.db import models
from account.models import CommonModel, User
from cinema.models import Show, SeatClass
# Create your models here.


class Booking(CommonModel):
    """
    This model is used to store the booking details.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, help_text='The person tickets booked by the user')
    show = models.ForeignKey(Show, on_delete=models.CASCADE, related_name='shows', help_text='The show booked by the user')
    seat_class = models.ForeignKey(SeatClass, on_delete=models.CASCADE, related_name='shows_seat_class',
                                   help_text='The seat class booked by the user')
    seat_number = models.CharField(max_length=255, help_text='The seat number booked by the user')
    no_of_tickets = models.DecimalField(max_digits=5, decimal_places=2, help_text='The number of the tickets booked by the user')
    service_fee = models.FloatField(default=0.0, help_text='The service fee for bank of the tickets booked by the user')
    total_cost = models.FloatField(default=0.0, help_text='The total cost of the tickets booked by the user')

    def __str__(self):
      return str(self.id)

    @classmethod
    def get_booking_details_all(cls):
        """
        Get all the booking details
        :param: None
        :return: Booking object
        :rtype: django.db.models.query.QuerySet
        """
        return cls.objects.filter(is_active=True)

    @classmethod
    def get_booked_count(cls, show_id):
        """
        Get the booking count by show
        :param: None
        :return: Booking object
        :rtype: django.db.models.query.QuerySet
        """
        from django.db.models import Sum
        return cls.objects.filter(show_id=show_id).aggregate(Sum('no_of_tickets')).get('no_of_tickets__sum', 0)