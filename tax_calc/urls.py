from django.urls import path
from tax_calc import views

urlpatterns = [
    path('', views.tax_calc, name='tax_calc'),
]
