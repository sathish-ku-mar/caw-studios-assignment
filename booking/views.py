from django.shortcuts import get_object_or_404
from .models import Booking
from .serializers import BookingCreateSerializer, BookingListSerializer
from rest_framework import status, viewsets
from rest_framework.response import Response
from django.http.request import QueryDict
from core.api_permission import UserAuthentication


class BookingViewSet(viewsets.ViewSet):
    """
        A simple ViewSet for the booking.
    """
    model = Booking
    serializer_class = BookingListSerializer
    queryset = model.get_booking_details_all()
    permission_classes = (UserAuthentication,)

    def list(self, request):
        """
            To list the booking
            URL Structure: /booking/
            Required Fields: None
        """

        queryset = self.model.get_booking_details_all()
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        """
            To book the movies
            URL Structure: /booking/
            Required Fields: user, show, seat_class, seat_number, no_of_tickets
        """
        data = QueryDict.dict(request.data)
        data['user'] = request.user.id
        serializer = BookingCreateSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)