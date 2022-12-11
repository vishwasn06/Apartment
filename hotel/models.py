from django.db import models
from django.conf import settings
# Create your models here.
class Location(models.Model):
    #h_id,h_name,owner ,location,rooms
    name = models.CharField(max_length=30,default="Apartment")
    owner = models.CharField(max_length=20,default="Abc")
    location = models.CharField(max_length=50,default="Udupi")
    state = models.CharField(max_length=50,default="Karnataka")
    country = models.CharField(max_length=50,default="India")
    def __str__(self):
        return self.name


class Rooms(models.Model):
    ROOM_STATUS = ( 
    ("1", "available"), 
    ("2", "not available"),    
    ) 

    ROOM_TYPE = ( 
    ("1", "premium"), 
    ("2", "deluxe"),
    ("3","basic"),    
    ) 

    #type,no_of_rooms,capacity,prices,Hotel
    room_type = models.CharField(max_length=50,choices = ROOM_TYPE)
    capacity = models.IntegerField()
    price = models.IntegerField()
    size = models.IntegerField()
    hotel = models.ForeignKey(Location, on_delete = models.CASCADE)
    status = models.CharField(choices =ROOM_STATUS,max_length = 15)
    roomnumber = models.IntegerField(unique=True)
    def __str__(self):
        return self.hotel.name

class Reservation(models.Model):
    check_in = models.DateField(auto_now =False)
    check_out = models.DateField()
    room = models.ForeignKey(Rooms, on_delete = models.CASCADE)
    guest = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete= models.CASCADE)
    
    booking_id = models.CharField(max_length=100,default="null")
    def __str__(self):
        return self.guest.username

