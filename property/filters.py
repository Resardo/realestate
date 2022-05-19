from cProfile import label
from dataclasses import field, fields
from re import L
from turtle import title
from unicodedata import name

import django_filters
from django_filters import DateFilter,RangeFilter

from .models import*



class PropertyFilter(django_filters.FilterSet):
    cmimi = RangeFilter(field_name="price",label="Cmimi")
    city = django_filters.ModelChoiceFilter(queryset=City.objects.all(),label='Qyteti')
    district = django_filters.ModelChoiceFilter(queryset=District.objects.filter(City,city_id=City.id), label="Zona")
    sip = RangeFilter(field_name="area",label="Siperfaqja",lookup_expr='gte')
   

    
    class Meta:
        model = Property
        fields = ['city','district','title','cmimi','sip','activity']

class PropertyFilter2(django_filters.FilterSet):
    city = django_filters.ModelChoiceFilter(queryset=City.objects.all(),label='city')
    district = django_filters.ModelChoiceFilter(queryset=District.objects.all(), label="Zona")
    titulli = django_filters.CharFilter(field_name='title',label='Keyword')
    class Meta:
        model = Property
        fields = ['city','titulli','district']
       
