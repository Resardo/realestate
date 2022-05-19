from cProfile import label
from dataclasses import field, fields


import django_filters
from django_filters import DateFilter,RangeFilter

from argparse import Action
from cProfile import label




from .models import *
PROPERTY_TYPE = (
        ("Apartament", "Apartament"),
        ("Vila", "Vila"),
        ("Store", "Dyqan"),
        ("Land", "Truall"),
        ("Garage", "Garazhd"),
    )
ACTION_OPTION = (
        ("Sale", "Shitje"),
        ("Rent", "Qera")
    )



class PropertyFilter(django_filters.FilterSet):

    city = django_filters.ModelChoiceFilter(queryset=City.objects.all(), label="City")
    district = django_filters.ModelChoiceFilter(queryset=District.objects.all(), label="District")
    title = django_filters.CharFilter(lookup_expr='icontains', label="Title")
    price__gt = django_filters.NumberFilter(field_name='price', lookup_expr='gt', label="Price min.")
    price__lt = django_filters.NumberFilter(field_name='price', lookup_expr='lt', label="Price max.")
    area__gt = django_filters.NumberFilter(field_name='area', lookup_expr='gt', label="Area min.")
    area__lt = django_filters.NumberFilter(field_name='area', lookup_expr='lt', label="Area max.")
    property_type = django_filters.ChoiceFilter(choices=PROPERTY_TYPE, label="Property Type")
    activity = django_filters.ChoiceFilter(choices=ACTION_OPTION, label="Action")
    
    class Meta:
        model = Property
        fields = ['city', 'district','activity','property_type','title', 'price__gt', 'price__lt', 'area__gt', 'area__lt']
        #label = ['City', 'District', 'Veprimi', 'Lloji prones', 'Titulli', 'Cmimi min.', 'Cmimi max.', 'Siperfaqja min.', 'Siperfaqja max.']
        exclude = ['description','addres_line', 'views', 'documents', 'status', 'updated_at','is_active',]

class PropertyFilter2(django_filters.FilterSet):
    city = django_filters.ModelChoiceFilter(queryset=City.objects.all(),label='city')
    district = django_filters.ModelChoiceFilter(queryset=District.objects.all(), label="Zona")
    titulli = django_filters.CharFilter(field_name='title',label='Keyword')
    class Meta:
        model = Property
        fields = ['city','titulli','district']
