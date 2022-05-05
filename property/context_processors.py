from .models import City, District

def cities(request):
    return{"cities": City.objects.all}

def districts(request):
    return{"districts": District.objects.all}