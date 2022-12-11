from django.contrib import admin

from .models import Location,Rooms,Reservation
# Register your models here.
admin.site.register(Location)
admin.site.register(Rooms)
admin.site.register(Reservation)
