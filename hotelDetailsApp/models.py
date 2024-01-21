from django.db import models

from user.models import User

# Create your models here.
class HotelDetails(models.Model):
    name = models.CharField(max_length = 40)
    place = models.CharField(max_length = 50)
    foodAvailability = models.BooleanField()
    quantity = models.IntegerField()
    type = models.TextField()
    contactNumber = models.IntegerField()
    foodVarieties = models.TextField()
    imagePath = models.TextField()
    username = models.ForeignKey(User,on_delete = models.CASCADE)