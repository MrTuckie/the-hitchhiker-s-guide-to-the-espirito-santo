from django.contrib import admin

from apps.place.models import Address, Place


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    pass


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    pass

