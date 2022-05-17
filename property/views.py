from asyncio.windows_events import NULL
from itertools import product
from msilib.schema import Property
from unicodedata import category
from django.http import Http404
from django.shortcuts import render
from django.shortcuts import get_object_or_404, render
from django.core.paginator import Paginator
from .filters import PropertyFilter,PropertyFilter2
from .models import Apartment, Garage, Land, Store, Villa, Property

def properties_all(request):
    properties = Property.objects.prefetch_related("property_image").filter(is_active=True)
    topProperties=Property.objects.prefetch_related("property_image").all().order_by('-views')
    lastAdded=Property.objects.prefetch_related("property_image").all().order_by('-created_at')

    print(topProperties)
    myFilter = PropertyFilter2(request.GET, queryset=properties) 
    properties = myFilter.qs
    return render(request, "home/index.html", {"properties" : properties, "topProperties" : topProperties, "lastAdded" : lastAdded, "myFilter" : myFilter})

def properties_list(request):
    properties = Property.objects.prefetch_related("property_image").filter(is_active=True)
    myFilter = PropertyFilter(request.GET, queryset=properties) 
    properties = myFilter.qs
    properties_paginator = Paginator(properties, 2)
    page_num= request.GET.get('page')
    page = properties_paginator.get_page(page_num)
    num_pages = "a" * page.paginator.num_pages
   
    
    return render(request, "home/properties.html", {"properties" : properties, "page" : page, "num_pages" : num_pages, "myFilter" : myFilter})

def land_all(request):
    properties = Land.objects.prefetch_related("property_image").filter(is_active=True)
    properties_paginator = Paginator(properties, 2)
    page_num= request.GET.get('page')
    page = properties_paginator.get_page(page_num)
    num_pages = "a" * page.paginator.num_pages
    return render(request, "home/properties.html", {"properties" : properties, "page" : page, "num_pages" : num_pages})

def store_all(request):
    properties = Store.objects.prefetch_related("property_image").filter(is_active=True)
    properties_paginator = Paginator(properties, 2)
    page_num= request.GET.get('page')
    page = properties_paginator.get_page(page_num)
    num_pages = "a" * page.paginator.num_pages
    return render(request, "home/properties.html", {"properties" : properties, "page" : page, "num_pages" : num_pages})

def garage_all(request):
    properties = Garage.objects.prefetch_related("property_image").filter(is_active=True)
    properties_paginator = Paginator(properties, 2)
    page_num= request.GET.get('page')
    page = properties_paginator.get_page(page_num)
    num_pages = "a" * page.paginator.num_pages
    return render(request, "home/properties.html", {"properties" : properties, "page" : page, "num_pages" : num_pages})

def villa_all(request):
    properties = Villa.objects.prefetch_related("property_image").filter(is_active=True)
    properties_paginator = Paginator(properties, 2)
    page_num= request.GET.get('page')
    page = properties_paginator.get_page(page_num)
    num_pages = "a" * page.paginator.num_pages
    return render(request, "home/properties.html", {"properties" : properties, "page" : page, "num_pages" : num_pages})

def apartment_all(request):
    properties = Apartment.objects.prefetch_related("property_image").filter(is_active=True)
    properties_paginator = Paginator(properties, 2)
    page_num= request.GET.get('page')
    page = properties_paginator.get_page(page_num)
    num_pages = "a" * page.paginator.num_pages
    return render(request, "home/properties.html", {"properties" : properties, "page" : page, "num_pages" : num_pages})


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


def contact_page(request):
    return render(request, 'home/conctact.html')

def aboutus(request):
    return render(request, 'home/about.html')

def politikat_privatesise(request):
    return render(request, 'home/politikat.html')