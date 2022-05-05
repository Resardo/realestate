from asyncio.windows_events import NULL
from itertools import product
from msilib.schema import Property
from unicodedata import category
from django.http import Http404
from django.shortcuts import render
from django.shortcuts import get_object_or_404, render
from .models import Apartment, Garage, Land, Store, Villa, Property

def properties_all(request):
    properties = Property.objects.prefetch_related("property_image").filter(is_active=True)
    topProperties=Property.objects.prefetch_related("property_image").all().order_by('-views')
    print(topProperties)
    return render(request, "home/index.html", {"properties" : properties, "topProperties" : topProperties})

def properties_list(request):
    properties = Property.objects.prefetch_related("property_image").filter(is_active=True)
    return render(request, "home/properties.html", {"properties" : properties})

def land_all(request):
    properties = Land.objects.prefetch_related("property_image").filter(is_active=True)
    return render(request, "home/properties.html", {"properties" : properties})

def store_all(request):
    properties = Store.objects.prefetch_related("property_image").filter(is_active=True)
    return render(request, "home/properties.html", {"properties" : properties})

def garage_all(request):
    properties = Garage.objects.prefetch_related("property_image").filter(is_active=True)
    return render(request, "home/properties.html", {"properties" : properties})

def villa_all(request):
    properties = Villa.objects.prefetch_related("property_image").filter(is_active=True)
    return render(request, "home/properties.html", {"properties" : properties})

def apartment_all(request):
    properties = Apartment.objects.prefetch_related("property_image").filter(is_active=True)
    return render(request, "home/properties.html", {"properties" : properties})


def property_detail(request, slug):
    queryset = Apartment.objects.filter(slug=slug, is_active=True)
    if queryset.exists():
        property = get_object_or_404(Apartment, slug=slug, is_active=True)
    else:
        queryset = Villa.objects.filter(slug=slug, is_active=True)
        if queryset.exists():
            property = get_object_or_404(Villa, slug=slug, is_active=True)
        else:
            queryset = Land.objects.filter(slug=slug, is_active=True)
            if queryset.exists():
                property = get_object_or_404(Land, slug=slug, is_active=True)
            else:
                queryset = Store.objects.filter(slug=slug, is_active=True)
                if queryset.exists():
                    property = get_object_or_404(Store, slug=slug, is_active=True)
                else:
                    queryset = Villa.objects.filter(slug=slug, is_active=True)
                    if queryset.exists():
                        property = get_object_or_404(Villa, slug=slug, is_active=True)

    return render(request, 'home/single.html', {"property": property})

def contact_page (request):
    return render(request, 'contact.html')