from django.contrib.auth.models import User, Group
from products_service.models import Product
from rest_framework import serializers
from . import tax_calc_api_call
from . import giphy_api_call

class ProductSerializer(serializers.HyperlinkedModelSerializer):
    tax = serializers.SerializerMethodField()
    gif_url = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ['url', 'name', 'description', 'price', 'location', 'material', 'timesofuse', 'brand', 'slogan', 'recycling', 'weight', 'tax','gif_url']

    def get_tax(self, obj):
        price = obj.price
        return tax_calc_api_call.get_tax(price)

    def get_gif_url(self,obj):
        searchterm = obj.name
        return giphy_api_call.get_gif_url(searchterm)