import os
from django.core.management.base import BaseCommand, CommandError
from products_service.models import Product
from products_service.serializers import ProductSerializer
import csv
import pysftp

class Command(BaseCommand):
    help = 'export all data in csv format'

    def handle(self, *args, **options):
        fieldnames = ProductSerializer.Meta.fields
        fieldnames.remove("url")
        fieldnames.remove("tax")
        fieldnames.remove("gif_url")
        products = Product.objects.all().values(*fieldnames)

        #with open('products.csv', 'w', newline='') as f:
         #   writer = csv.writer(f)
          #  writer.writerows(products)

        with open('products.csv', 'w', newline='') as csvfile:

            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            writer.writerows(products)

        cnopts = pysftp.CnOpts()
        cnopts.hostkeys = None #not advised for production, really not.
        srv = pysftp.Connection(host=os.environ.get("SFTP_HOST", ""), username=os.environ.get("SFTP_USERNAME", ""),
                                password=os.environ.get("SFTP_PASSWORD", ""), cnopts=cnopts) #log="./temp/pysftp.log"

        with srv.cd('upload'):  # chdir to upload
            srv.put('products.csv')  # upload file to sftpserver

        # Closes the connection
        srv.close()
        self.stdout.write(self.style.SUCCESS('Successfully exported and uploaded csv to sftp server'))