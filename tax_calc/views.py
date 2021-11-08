from django.contrib.auth.models import User, Group
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer, TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST

from tax_calc.models import Product
from tax_calc.serializers import UserSerializer, GroupSerializer, ProductSerializer

@api_view()#by default only get requests are allowed
@renderer_classes([TemplateHTMLRenderer,JSONRenderer])
def tax_calc(request):
    if not 'cent' in request.query_params:
        return Response({'message':"#kein price kein request lol"},status= HTTP_400_BAD_REQUEST, template_name='400.html')
    try:
        price = int(request.query_params['cent'])
    except ValueError:
        return Response ({'message':"bitte int angeben"},status= HTTP_400_BAD_REQUEST, template_name='400.html')
    tax = price*0.19
    context = {
        'price':price,
        'tax':tax
    }
    return Response(context, template_name='tax_calc.html')

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

class ProductViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows products to be viewed or edited.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]