from dataclasses import fields

import django_filters
from django_filters import DateFilter

from .models import*

class PropertyFilter(django_filters.FilterSet):
    class Meta:
        model = Property
        fields = '__all__'
        exclude = ['description','addres_line', 'area', 'views', 'documents', 'status', 'activity', 'updated_at','is_active','price' ]
