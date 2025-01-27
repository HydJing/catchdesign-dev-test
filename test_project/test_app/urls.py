from django.urls import path
from test_app.views import CustomerListView, customer_list

urlpatterns = [
    path('api/customers/', CustomerListView.as_view(), name='customer-list'),
    path('customers/', customer_list, name='customer-web'),
]
