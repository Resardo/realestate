from dataclasses import fields
from unicodedata import name

import django_filters
from django_filters import DateFilter,RangeFilter

from .models import*



class PropertyFilter(django_filters.FilterSet):
    price = RangeFilter(field_name="price")
    class Meta:
        model = Property
        fields = '__all__'
        exclude = ['description','addressS_line', 'area', 'views', 'documents', 'status', 'activity', 'updated_at','is_active','price' ]

class PropertyFilter2(django_filters.FilterSet):
    
    class Meta:
        model = Property
        fields = '__all__'
        exclude = ['slug','created_at','description','address_line', 'area', 'views', 'documents', 'status', 'activity', 'updated_at','is_active','price' ]
