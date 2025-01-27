from django.db import models

# Create your models here.
from django.db import models

class Customer(models.Model):
    id = models.AutoField(primary_key=True)  # Auto-incremented ID
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    gender = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')])
    ip_address = models.GenericIPAddressField()
    company = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    website = models.URLField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
