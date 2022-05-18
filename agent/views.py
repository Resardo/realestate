from django.shortcuts import render, get_object_or_404
from .models import User
from property.models import Property
from django.core.paginator import Paginator

def agent_all(request):
    agents = User.objects.all()
    for a in agents:
        print(a.get_absolute_url)
    return render(request, 'home/ourteam.html', {"agents": agents})

def agent_properties(request, slug=None):
    agent = get_object_or_404(User, slug=slug)
    properties = Property.objects.filter(created_by=agent)
    properties_paginator = Paginator(properties, 2)
    page_num= request.GET.get('page')
    page = properties_paginator.get_page(page_num)
    num_pages = "a" * page.paginator.num_pages
    print(agent)
    print(properties)
    return render(request, 'home/agent_properties.html', {'agent': agent, 'properties': properties, "page" : page, "num_pages" : num_pages,}) 