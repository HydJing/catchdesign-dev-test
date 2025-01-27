from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import PageNumberPagination
from test_app.models import Customer
from test_app.serializers import CustomerSerializer

class CustomerPagination(PageNumberPagination):
    page_size = 10  # number of items per page
    page_size_query_param = 'page_size'
    max_page_size = 100

class CustomerListView(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    pagination_class = CustomerPagination

     # Add filtering capability
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter)
    filterset_fields = ['city', 'company', 'gender']  # Allow filtering by these fields
    ordering_fields = ['id', 'last_name', 'email']
    ordering = ['id']
    