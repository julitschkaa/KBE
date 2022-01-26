from django.core.management.base import BaseCommand, CommandError
from products_service.models import Product
import csv

class Command(BaseCommand):
    help = 'export all data in csv format'

    def handle(self, *args, **options):

        products = Product.objects.all().values_list()

        with open('products.csv', 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerows(products)

        self.stdout.write(self.style.SUCCESS('Successfully exported csv'))