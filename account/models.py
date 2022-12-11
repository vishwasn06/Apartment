from typing import AbstractSet
from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import AbstractBaseUser, AbstractUser, BaseUserManager
from django.db.models.fields.files import ImageField

#from django.contrib.auth.models import PermissionsMixin


class User(AbstractUser):
   
    email                   = models.EmailField(verbose_name="email", max_length=60, unique=True)
    is_guest = models.BooleanField(default=False)
    is_resident = models.BooleanField(default=False)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=10)

class Resident(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, primary_key = True)
    aadhar = models.CharField(max_length=12)
    Room = models.IntegerField(default=True,help_text = "Enter your room Number")
    
class Guest(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, primary_key = True)
    aadhar = models.CharField(max_length=12)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self):
        super().save()

        img = ImageField.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)