from django.contrib.auth.models import User, Group
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer, TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST

@api_view()#by default only get requests are allowed
@renderer_classes([TemplateHTMLRenderer,JSONRenderer])
def tax_calc(request):
    if not 'cent' in request.query_params:
        return Response({'message':"the correct API endpoint is 'mwst/?cent=<int>' "},status= HTTP_400_BAD_REQUEST, template_name='400.html')
    try:
        price = int(request.query_params['cent'])
    except ValueError:
        return Response ({'message':"please enter Integer after '?cent='"},status= HTTP_400_BAD_REQUEST, template_name='400.html')
    tax = price*0.19
    context = {
        'price':price,
        'tax':tax
    }
    return Response(context, template_name='tax_calc.html')