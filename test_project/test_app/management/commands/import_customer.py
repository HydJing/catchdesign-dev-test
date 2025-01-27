import csv
from django.core.management.base import BaseCommand
from test_app.models import Customer

class Command(BaseCommand):
    help = 'Load customer data from CSV into the database'

    def handle(self, *args, **kwargs):
        try:
            with open('./data/customers.csv', 'r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    Customer.objects.update_or_create(
                        id=row['id'],
                        defaults={
                            'first_name': row['first_name'],
                            'last_name': row['last_name'],
                            'email': row['email'],
                            'gender': row['gender'],
                            'ip_address': row['ip_address'],
                            'company': row['company'],
                            'city': row['city'],
                            'title': row['title'],
                            'website': row['website'],
                        }
                    )
            self.stdout.write(self.style.SUCCESS('Successfully loaded customer data.'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error: {e}'))
