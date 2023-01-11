from django.db import models
from django.conf import settings

# Create your models here.


class Room(models.Model):
    ROOM_CATEGORIES = (
        ('YAC', 'AC'),
        ('NAC', 'NO-AC'),
        ('LUX', 'LUXURY'),
        ('KIN', 'KING'),
        ('QEE', 'QUEEN'),
    )
    number = models.IntegerField()
    catergory = models.CharField(max_length=3, choices=ROOM_CATEGORIES)
    beds = models.IntegerField()
    capacity = models.IntegerField()

    def __str__(self):
        return (f'{self.number}. {self.catergory} with {self.beds} bed(s) for {self.capacity} people')


class Booking(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    check_in = models.DateTimeField()
    check_out = models.DateTimeField()

    def __str__(self):
        return f'{self.user} has booked {self.room} from {self.check_in} to {self.check_out}'
