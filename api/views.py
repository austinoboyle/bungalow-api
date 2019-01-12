from rest_framework import generics, filters
from api.models import Rental
from django_filters.rest_framework import DjangoFilterBackend
from api.serializers import RentalSerializer


class RentalList(generics.ListCreateAPIView):
    queryset = Rental.objects.all()
    serializer_class = RentalSerializer
    filter_backends = (filters.OrderingFilter, DjangoFilterBackend,)
    filter_fields = '__all__'
    filter_fields = ('bathrooms', 'bedrooms',
                     'home_type', 'zillow_id', 'city', 'state', 'zipcode')
    ordering_fields = ('price', 'home_size', 'rent_price',
                       'rentzestimate_amount', 'zestimate_amount')


class SingleRental(generics.RetrieveUpdateDestroyAPIView):
    queryset = Rental.objects.all()
    serializer_class = RentalSerializer
