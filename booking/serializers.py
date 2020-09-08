from rest_framework import serializers
from .models import Booking
from movie.serializers import MovieSerializer
from cinema.serializers import ShowSerializer, SeatSerializer


class BookingListSerializer(serializers.ModelSerializer):
    show = ShowSerializer()
    seat_class = SeatSerializer()

    class Meta:
        model = Booking
        fields = ('id', 'user', 'show', 'seat_class', 'seat_number', 'no_of_tickets', 'service_fee', 'total_cost')
        read_only_fields = ('id',)


class BookingCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Booking
        fields = ('id', 'user', 'show', 'seat_class', 'seat_number', 'no_of_tickets', 'service_fee', 'total_cost')
        read_only_fields = ('id',)