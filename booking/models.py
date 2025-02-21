from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Room(models.Model):
    number = models.CharField(max_length=20)
    capacity = models.IntegerField()
    locating = models.TextField()


    def __str__(self):
        return f"{self.number} - {self.capacity}"

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name="bookings")
    room = models.ForeignKey(Room, on_delete=models.CASCADE,related_name="bookings")
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    creating_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.room} - {self.user}"
