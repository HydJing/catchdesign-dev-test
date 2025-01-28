from rest_framework import serializers
from test_app.models import Customer

"""Serializer for load data into DB."""
class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['id', 'first_name', 'last_name', 'email', 'gender', 'ip_address', 'company', 'city', 'title', 'website']
