from django.contrib.auth.models import User, Group
from products_service.models import Product
from rest_framework import serializers

class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = ['url', 'name', 'description', 'price', 'location', 'material', 'timesofuse', 'brand', 'slogan', 'recycling', 'weight']