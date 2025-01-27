from django.urls import path
from test_app.views import CustomerListView

urlpatterns = [
    path('api/customers/', CustomerListView.as_view(), name='customer-list'),
]
