from django.contrib import admin

from .models import *

admin.site.register(City)
admin.site.register(District)


class PropertyImageInline(admin.TabularInline):
    model = PropertyImage


@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    inlines = [
        PropertyImageInline,
    ]

@admin.register(Apartment)
class ApartmentAdmin(admin.ModelAdmin):
    inlines = [
        PropertyImageInline,
    ]

@admin.register(Villa)
class VillaAdmin(admin.ModelAdmin):
    inlines = [
        PropertyImageInline,
    ]

@admin.register(Garage)
class GarageAdmin(admin.ModelAdmin):
    inlines = [
        PropertyImageInline,
    ]

@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    inlines = [
        PropertyImageInline,
    ]

@admin.register(Land)
class LandAdmin(admin.ModelAdmin):
    inlines = [
        PropertyImageInline,
    ]